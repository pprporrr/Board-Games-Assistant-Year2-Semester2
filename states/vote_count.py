import os, time, pygame
from states.state import State
from states.hand_count import hand_count

from models.experimental import attempt_load
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

class vote_count(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.start_count = False
        
    def update(self, delta_time, action):
        
        if self.start_count == False:
            self.start_count = True
            count_vote()
            new_state = hand_count(self.game)
            new_state.enter_state()
        
    def render(self, display):
        display.fill((0, 0, 0))
        self.game.draw_text(display, "Fucntion: Detect Vote Card", 20, (255, 255, 255), (800, 450))
        # self.Text_1.draw_text(display)
        
        
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def countObject(predictions, targetClass):
    objectCounts = {targetClass: 0}
    for prediction in predictions:
        if prediction["class"] == targetClass:
            objectCounts[targetClass] += 1
    return objectCounts

def testobjectDetection(imgPath,targetClass):
    predictions = objectModel.predict(f"{imgPath}")
    classCounts = countObject(predictions, targetClass)
    return classCounts[targetClass], predictions

def open_image(imgPath):
    # open method used to open different extension image file
    im = Image.open(imgPath) 
    
    # This method will show image in any image viewer 
    im.show()
    return

def count_vote():
    
    # count down
    clear()
    # start_time = time.time()
    for i in range(5, 0, -1):
        time.sleep(1)
        print(f"Start count in {i}")
        
    #Object Detection Function
    tagetClass = "success"
    
        # for already image
    imgPathObj = "backup\IMG_6153.JPG"
    
        # for img from webcam
    # cam_port = 0
    # cam = cv2.VideoCapture(cam_port)
    # result, image = cam.read()
    # cv2.imwrite("temp.png", image)
    # imgPathObj = "temp.png"
    
    objectDetectresult, resultsJson = testobjectDetection(imgPathObj, tagetClass)
    print(f"Number Of Objects [{tagetClass}]:", objectDetectresult)
    open_image(imgPathObj) # show image
        
        # result
    # print(resultsJson)
    # print(time.time() - start_time)
    time.sleep(5)
    
    
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
        