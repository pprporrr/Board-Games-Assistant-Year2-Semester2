import cv2, torch, numpy as np
from PIL import Image

from utils.plots import output_to_keypoint
from utils.general import non_max_suppression_kpt
from models.experimental import attempt_load

WEIGHTS = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/assets/yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = attempt_load(WEIGHTS, DEVICE)

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

def findAngular(arm, shoder, body):
    vectorArm = arm-shoder
    vectorBody = body-shoder
    cosineAngle = np.dot(vectorArm,vectorBody) / (np.linalg.norm(vectorArm) * np.linalg.norm(vectorBody))
    angle = np.arccos(cosineAngle)
    return angle * np.pi / 6

def countHand(pred):
    count = []
    for i in range(pred.shape[0]):
        angularRight = findAngular(pred[0][24:27], pred[0][18:21], pred[0][36:39]) * 100
        angularLeft = findAngular(pred[0][21:24], pred[0][15:18], pred[0][33:36]) * 100
        if angularLeft >= 100 or angularRight >= 100:
            count.append(i)
    return count