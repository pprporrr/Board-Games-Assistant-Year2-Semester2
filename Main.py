from utils.general import non_max_suppression_kpt
from models.experimental import attempt_load
from utils.plots import plot_skeleton_kpts
from utils.plots import output_to_keypoint
import cv2, torch, time, numpy as np
from roboflow import Roboflow
from os import system, name
from PIL import Image

print("Loading...")
WEIGHTS = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/assets/yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
handModel = attempt_load(WEIGHTS, DEVICE)
rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon")
questModel = project.version(4).model
rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon-tableau")
tableauModel = project.version(3).model

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def findAngular(arm, shoder, body):
    vectorArm = arm-shoder
    vectorBody = body-shoder
    cosineAngle = np.dot(vectorArm,vectorBody) / (np.linalg.norm(vectorArm) * np.linalg.norm(vectorBody))
    angle = np.arccos(cosineAngle)
    return angle * np.pi / 6

def predictKeypoints(image, imageSize=640, confThresh=0.25, iouThresh=0.65):
    image = np.asarray(image)
    H, W = image.shape[:2]
    image = cv2.resize(image, (imageSize, imageSize))
    imagePt = torch.from_numpy(image).permute(2, 0, 1).to(DEVICE)
    imagePt = imagePt.float() / 255.0
    with torch.no_grad():
        predictions = handModel(imagePt[None], augment = False)[0]
    predictions = non_max_suppression_kpt(
        predictions, confThresh, iouThresh, 
        nc = handModel.yaml["nc"], nkpt = handModel.yaml["nkpt"], kpt_label = True
    )
    predictions = output_to_keypoint(predictions)
    predictions = predictions[:, 7:]
    predictions[:, 0::3] *= W / imageSize
    predictions[:, 1::3] *= H / imageSize
    return predictions

def countHand(predictions):
    count = []
    for i in range(predictions.shape[0]):
        angularRight = findAngular(predictions[0][24:27], predictions[0][18:21], predictions[0][36:39]) * 100
        angularLeft = findAngular(predictions[0][21:24], predictions[0][15:18], predictions[0][33:36]) * 100
        if angularLeft >= 100 or angularRight >= 100:
            count.append(i)
    return count

def testcountHand(path):
    image = Image.open(path)
    predictions = predictKeypoints(image)
    image = np.asarray(image)
    handUp = countHand(predictions)
    for idx in handUp:
        plot_skeleton_kpts(image, predictions[idx].T, 3)
    image = Image.fromarray(image)
    return len(handUp), image

def countObject(predictions, targetClass):
    objectCounts = {targetClass: 0}
    for prediction in predictions:
        if prediction["class"] == targetClass:
            objectCounts[targetClass] += 1
    return objectCounts

def questDetection(imgPath, targetClass):
    predictions = questModel.predict(f"{imgPath}")
    classCounts = countObject(predictions, targetClass)
    return classCounts[targetClass], predictions

def tableauDetection(imgPath, targetClass):
    predictions = tableauModel.predict(f"{imgPath}")
    classCounts = countObject(predictions, targetClass)
    if classCounts[targetClass] > 0:
        if targetClass == "Tableau10":
            numPlayer = 10
        elif targetClass == "Tableau9":
            numPlayer = 9
        elif targetClass == "Tableau8":
            numPlayer = 8
        elif targetClass == "Tableau7":
            numPlayer = 7
        elif targetClass == "Tableau6":
            numPlayer = 6
        elif targetClass == "Tableau5":
            numPlayer = 5
    return numPlayer, predictions

if __name__ == "__main__":
    print("Done")
    clear()
    
    startTime1 = time.time()
    print("Tableau Detection Function")
    tagetClass = "Tableau6"
    imgPathObj = "/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/backup/Tableau6.JPG"
    tableauDetectresult, tableauresultsJson = tableauDetection(imgPathObj, tagetClass)
    print(f"Number Of Players [{tagetClass}]:", tableauDetectresult)
    print("Run Time: ", time.time() - startTime1, "\n")
    
    startTime2 = time.time()
    print("Quest Detection Function")
    tagetClassSuccess = "success"
    tagetClassFail = "fail"
    imgPathObj = "/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/backup/4success_1fail.jpg"
    questDetectresultSuccess, questresultsJson = questDetection(imgPathObj, tagetClassSuccess)
    questDetectresultFail, questresultsJson = questDetection(imgPathObj, tagetClassFail)
    print(f"Number Of Success Cards [{tagetClassSuccess}]:", questDetectresultSuccess)
    print(f"Number Of Fail Cards [{tagetClassFail}]:", questDetectresultFail)
    print("Run Time: ", time.time() - startTime2, "\n")
    
    startTime3 = time.time()
    print("Cound Hand Function")
    imgPathHand = "/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/backup/Player5_hand_up.jpg"
    countHandResult, countedImg = testcountHand(imgPathHand)
    print("Hand Up: ", countHandResult)
    countedImg.show()
    print("Run Time: ", time.time() - startTime3, "\n")