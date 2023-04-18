#18 APR
#from detectionFunction import objectDetection, delete
#from counthandFunction import predictKeypoints, countHand
from utils.general import non_max_suppression_kpt
from models.experimental import attempt_load
from utils.plots import plot_skeleton_kpts
from utils.plots import output_to_keypoint
import cv2, torch, numpy as np
from roboflow import Roboflow
from PIL import Image

WEIGHTS = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/assets/yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = attempt_load(WEIGHTS, DEVICE)

def findAngular(arm, shoder, body):
    vectorArm = arm-shoder
    vectorBody = body-shoder
    cosineAngle = np.dot(vectorArm,vectorBody) / (np.linalg.norm(vectorArm) * np.linalg.norm(vectorBody))
    angle = np.arccos(cosineAngle)
    return angle * np.pi / 6

def countObject(predictions, targetClass):
    objectCounts = {targetClass: 0}
    for prediction in predictions:
        if prediction["class"] == targetClass:
            objectCounts[targetClass] += 1
    return objectCounts

def countHand(pred):
    count = []
    for i in range(pred.shape[0]):
        angularRight = findAngular(pred[0][24:27], pred[0][18:21], pred[0][36:39]) * 100
        angularLeft = findAngular(pred[0][21:24], pred[0][15:18], pred[0][33:36]) * 100
        if angularLeft >= 100 or angularRight >= 100:
            count.append(i)
    return count

def predictKeypoints(image, imageSize=640, confThresh=0.25, iouThresh=0.65):
    image = np.asarray(image)
    H, W = image.shape[:2]
    image = cv2.resize(image, (imageSize, imageSize))
    imagePt = torch.from_numpy(image).permute(2, 0, 1).to(DEVICE)
    imagePt = imagePt.float() / 255.0
    with torch.no_grad():
        pred = model(imagePt[None], augment = False)[0]
    pred = non_max_suppression_kpt(
        pred, confThresh, iouThresh, 
        nc = model.yaml["nc"], nkpt=model.yaml["nkpt"], kpt_label = True
    )
    pred = output_to_keypoint(pred)
    pred = pred[:, 7:]
    pred[:, 0::3] *= W / imageSize
    pred[:, 1::3] *= H / imageSize
    return pred

def testobjectDetection(imgPath,targetClass):
    rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
    project = rf.workspace().project("yolov5-avalon")
    model = project.version(3).model
    predictions = model.predict(f"{imgPath}")
    classCounts = countObject(predictions, targetClass)
    return classCounts[targetClass], predictions

def testcountHand(path):
    image = Image.open(path)
    pred = predictKeypoints(image)
    image = np.asarray(image)
    handUp = countHand(pred)
    for idx in handUp:
        plot_skeleton_kpts(image, pred[idx].T, 3)
    image = Image.fromarray(image)
    return len(handUp), image

#Object Detection Function
imgPathObj = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/backup/IMG_6153.JPG"
objectDetectresult, resultsJson = testobjectDetection(imgPathObj, "success")
print("Number Of Objects: ", objectDetectresult)
print(resultsJson)

#Cound Hand Function
imgPathHand = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/backup/test5.jpg"
countHandResult, countedImg = testcountHand(imgPathHand)
print("Hand Up: ", countHandResult)
countedImg.show()

"""Use in detectionFunction.py
path2Folder = "assets/captureIMG"
objectDetectResult = objectDetection(path2Folder, "Vote", "success", 1)
print("Number Of Objects: ", objectDetectResult)
delete(path2Folder)"""