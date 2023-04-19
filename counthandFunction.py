import cv2, torch, sys, pygame, numpy as np
from utils.general import non_max_suppression_kpt
from models.experimental import attempt_load
from utils.plots import output_to_keypoint
from pygame.locals import *

def findAngular(arm, shoder, body):
    vectorArm = arm - shoder
    vectorBody = body - shoder
    cosineAngle = np.dot(vectorArm, vectorBody) / (np.linalg.norm(vectorArm) * np.linalg.norm(vectorBody))
    angle = np.arccos(cosineAngle)
    return angle * np.pi / 6

def countHand(pred):
    count = []
    for i in range(pred.shape[0]):
        angularRight = findAngular(pred[0][24:27],pred[0][18:21],pred[0][36:39]) * 100
        angularLeft = findAngular(pred[0][21:24],pred[0][15:18],pred[0][33:36]) * 100
        if angularLeft >= 100 or angularRight >= 100:
            count.append((int(pred[i][0]), int(pred[i][1])))
    return count

def predictKeypoints(image, imageSize=640, confThresh=0.25, iouThresh=0.65):
    image = np.asarray(image)
    h, w = image.shape[:2]
    image = cv2.resize(image, (imageSize, imageSize))
    imagePt = torch.from_numpy(image).permute(2, 0, 1).to(DEVICE)
    imagePt = imagePt.float() / 255.0
    with torch.no_grad():
        pred = model(imagePt[None], augment=False)[0]
    pred = non_max_suppression_kpt(
        pred, confThresh, iouThresh, 
        nc = model.yaml['nc'], nkpt = model.yaml['nkpt'], kpt_label = True
    )
    pred = output_to_keypoint(pred)
    pred = pred.reshape(-1, 58)
    pred = pred[:, 7:]
    pred[:, 0::3] *= w / imageSize
    pred[:, 1::3] *= h / imageSize
    return pred

WEIGHTS = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/assets/yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = attempt_load(WEIGHTS, DEVICE)

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    pred = predictKeypoints(frame)
    handUp = countHand(pred)

    for kpts in handUp:
        cv2.circle(frame, (kpts[0], kpts[1] - 50), 10, (0, 0, 255), -1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.rotate(frame, -90)
    
    screen.blit(frame, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            cap.release()
            pygame.quit()
            sys.exit()