import cv2
import pygame
from pygame.locals import *

import sys

import cv2
import numpy as np
import torch
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from torchvision import transforms

from models.experimental import attempt_load
from utils.datasets import letterbox
from utils.general import non_max_suppression_kpt
from utils.plots import output_to_keypoint, plot_skeleton_kpts

#count hand function
#===================================================================================================
def find_angular(arm,shoder,body):
    vector_arm = arm-shoder
    vector_body = body-shoder
    # print(vector_arm,(np.linalg.norm(vector_arm)))
    # print(vector_body,(np.linalg.norm(vector_body)))
    # print(np.dot(vector_arm,vector_body))
    cosine_angle = np.dot(vector_arm,vector_body) / (np.linalg.norm(vector_arm) * np.linalg.norm(vector_body))
    # print(cosine_angle)
    angle = np.arccos(cosine_angle)
    return angle*np.pi/6

def count_hand(pred):
    count=[]
    for i in range(pred.shape[0]):
        angular_right=find_angular(pred[0][24:27],pred[0][18:21],pred[0][36:39])*100
        angular_left=find_angular(pred[0][21:24],pred[0][15:18],pred[0][33:36])*100
        if angular_left>=100 or angular_right>=100:
            count.append(i)
    return count
#========================================================================================================

def predict_keypoints(image, image_size=640, conf_thresh=0.25, iou_thresh=0.65):
    image = np.asarray(image)
    
    # Resize image to the inference size
    ori_h, ori_w = image.shape[:2]
    image = cv2.resize(image, (image_size, image_size))
    
    # Transform image from numpy to torch format
    image_pt = torch.from_numpy(image).permute(2, 0, 1).to(DEVICE)
    image_pt = image_pt.float() / 255.0
    
    # Infer
    with torch.no_grad():
        pred = model(image_pt[None], augment=False)[0]
    
    # NMS
    pred = non_max_suppression_kpt(
        pred, conf_thresh, iou_thresh, 
        nc=model.yaml['nc'], nkpt=model.yaml['nkpt'], kpt_label=True
    )
    pred = output_to_keypoint(pred)
    
    # Drop
    pred = pred.reshape(-1, 58)
    pred = pred[:, 7:]
    
    # Resize boxes to the original image size
    pred[:, 0::3] *= ori_w / image_size
    pred[:, 1::3] *= ori_h / image_size
    
    return pred

WEIGHTS = "yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
IMAGE_SIZE = 640
model = attempt_load(WEIGHTS, DEVICE)

pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Get a frame from the camera
    ret, frame = cap.read()
    pred = predict_keypoints(frame, image_size=IMAGE_SIZE)
    hand_up=count_hand(pred)

    for kpts in hand_up:
        print(kpts)
        cv2.circle(frame,(int(kpts[0]),int(kpts[1])-50),10,(0,0,255),-1)

    # Convert the frame to a Pygame surface
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.rotate(frame, -90)

    # Display the frame on the screen
    screen.blit(frame, (0, 0))
    pygame.display.flip()
    #clock.tick(30)

    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            cap.release()
            pygame.quit()
            sys.exit()
