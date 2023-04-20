import os, time, pygame
from states.state import State

from utils.general import non_max_suppression_kpt
from models.experimental import attempt_load
from utils.plots import plot_skeleton_kpts
from utils.plots import output_to_keypoint
import cv2, torch, time, numpy as np
from roboflow import Roboflow
from os import system, name
from PIL import Image

WEIGHTS = "assets\yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
handModel = attempt_load(WEIGHTS, DEVICE)
rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon")
objectModel = project.version(4).model

class hand_count(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.start_count = False
        
    def update(self, delta_time, action):
        
        if self.start_count == False:
            self.start_count = True
            count_hand()
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        # self.Text_1.draw_text(display)
        
        
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

def testcountHand(image):
    # image = Image.open(path) # If you want to use path can uncommend it
    predictions = predictKeypoints(image)
    image = np.asarray(image)
    handUp = countHand(predictions)
    for idx in handUp:
        plot_skeleton_kpts(image, predictions[idx].T, 3)
    image = Image.fromarray(image)
    return len(handUp), image


def count_hand():
    # print("Done")
    # clear()
    start_time = time.time()
    for i in range(10, 0, -1):
        time.sleep(1)
        print(f"Start count in {i}")
        
    #Cound Hand Function
    # imgPathHand = r"backup\test5.jpg"
    
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
        
    # countHandResult, countedImg = testcountHand(imgPathHand)
    countHandResult, countedImg = testcountHand(image)
    print("Hand Up: ", countHandResult)
    countedImg.show()
    # print(time.time() - start_time)
        
class Button:
    def __init__(self, text, text_font, Text_size, Text_color, button_color, width_height, pos):
        gui_font = pygame.font.Font(os.path.join("assets", "font", text_font), Text_size)
        self.pos = pos
        self.pressed = False
        self.width_height = width_height
        self.top_rect = pygame.Rect(pos, width_height)
        self.top_color = button_color
        self.text_surf = gui_font.render(text, True, Text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.top_color, self.top_rect)
        surface.blit(self.text_surf, self.text_rect)
        
    def draw_image(self, surface, image):
        image = pygame.image.load(os.path.join("assets", "Detect_pic", image))
        image = pygame.transform.scale(image, self.width_height)
        surface.blit(image, self.pos)
        
    def draw_with_border(self, surface, border, border_color):
        surf = pygame.Surface((self.width_height[0]+border*2, self.width_height[1]+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.top_color, (border, border, self.width_height[0], self.width_height[1]), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, self.width_height[0], self.width_height[1]), 1)
        surface.blit(surf, self.top_rect)
        surface.blit(self.text_surf, self.text_rect)
        
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()        
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True

            else:
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    
    def draw_text(self, surface):
        text_rect = self.text_surf.get_rect(topleft = self.pos)
        surface.blit(self.text_surf, text_rect)
        