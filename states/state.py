import pygame, os
from utils.general import non_max_suppression_kpt
from models.experimental import attempt_load
from utils.plots import plot_skeleton_kpts
from utils.plots import output_to_keypoint
import cv2, torch, time, math, numpy as np
from roboflow import Roboflow
from os import system, name
from PIL import Image

WEIGHTS = "assets\yolov7-w6-pose.pt"
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
handModel = attempt_load(WEIGHTS, DEVICE)
rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon")
objectModel = project.version(4).model

class State():
    def __init__(self, game):
        self.game = game
        # self.button = button
        self.prev_state = None
        
    def update(self, delta_time, check_clicked):
        pass
    
    def render(self, surface):
        pass
    
    def enter_state(self):
        if len(self.game.state_stack) > 1:
            self.prev_state = self.game.state_stack[-1]
            
        self.game.state_stack.append(self)
        
    def exit_state(self):
        self.game.state_stack.pop()
        
class Button:
    def __init__(self, text, text_font, Text_size, Text_color, button_color, width_height, pos):
        gui_font = pygame.font.Font(os.path.join("assets", "font", text_font), Text_size)
        self.text = text
        self.text_font = text_font
        self.Text_size = Text_size
        self.Text_color = Text_color
        self.button_color = button_color
        self.top_color = button_color
        self.pos = pos
        self.pressed = False
        self.width_height = width_height
        self.top_rect = pygame.Rect(pos, width_height)
        self.text_surf = gui_font.render(text, True, Text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.top_color, self.top_rect)
        surface.blit(self.text_surf, self.text_rect)
        
    def draw_image(self, surface, image):
        image = pygame.image.load(os.path.join("assets", "pic", image)).convert_alpha()
        temp = pygame.transform.scale(image, self.width_height)
        try:
            # button_color = list(self.top_color)
            if self.button_color[3] is not None:
                temp = pygame.Surface((image.get_width(), image.get_height())).convert_alpha()
                temp.blit(surface, (-self.pos[0], -self.pos[1]))
                temp.blit(image, (0, 0))
                temp.set_alpha(self.button_color[3])
        except:
            pass
        surface.blit(temp, self.pos)
        
    # def blit_alpha(target, source, location, opacity):
    #     x = location[0]
    #     y = location[1]
    #     temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    #     temp.blit(target, (-x, -y))
    #     temp.blit(source, (0, 0))
    #     temp.set_alpha(opacity)        
    #     target.blit(temp, location)
    #     # blit_alpha(screen, happy, (100, 100), 128)
        
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
        try:
            self.Text_color = list(self.Text_color)
            if self.Text_color[3] is not None:
                gui_font = pygame.font.Font(os.path.join("assets", "font", self.text_font), self.Text_size)
                self.text_surf = gui_font.render(self.text, True, self.Text_color)
            self.text_surf.set_alpha(self.Text_color[3])
        except:
            pass
        text_rect = self.text_surf.get_rect(topleft = self.pos)
        surface.blit(self.text_surf, text_rect)
        
    def draw_text_center(self, surface):
        try:
            self.Text_color = list(self.Text_color)
            if self.Text_color[3] is not None:
                gui_font = pygame.font.Font(os.path.join("assets", "font", self.text_font), self.Text_size)
                self.text_surf = gui_font.render(self.text, True, self.Text_color)
            self.text_surf.set_alpha(self.Text_color[3])
        except:
            pass
        text_rect = self.text_surf.get_rect(center = (self.pos))
        surface.blit(self.text_surf, text_rect)
        
    def draw_arc(self, surface, start_angle, stop_angle, arc_radius, tickness):
        surf = pygame.Surface((self.width_height[0], self.width_height[1]), pygame.SRCALPHA)
        for i in range(start_angle, math.ceil(stop_angle), 1):
            angle = math.radians(i)
            x = (self.width_height[0]/2) + arc_radius * math.cos(angle)
            y = (self.width_height[1]/2) + arc_radius * math.sin(angle)
            pygame.draw.circle(surf, self.Text_color, (int(x), int(y)), tickness)
            
        # surface.blit(surf, self.top_rect)
        # surface.blit(self.text_surf, self.text_rect)
        text_rect = self.text_surf.get_rect(topleft = self.pos)
        surface.blit(surf, text_rect)
        
class Dectect():
    def __init__(self, game):
        self.game = game
        
    def clear(self):
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def findAngular(self, arm, shoder, body):
        vectorArm = arm-shoder
        vectorBody = body-shoder
        cosineAngle = np.dot(vectorArm,vectorBody) / (np.linalg.norm(vectorArm) * np.linalg.norm(vectorBody))
        angle = np.arccos(cosineAngle)
        return angle * np.pi / 6

    def predictKeypoints(self, image, imageSize=640, confThresh=0.25, iouThresh=0.65):
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

    def countHand(self, predictions):
        count = []
        for i in range(predictions.shape[0]):
            angularRight = self.findAngular(predictions[0][24:27], predictions[0][18:21], predictions[0][36:39]) * 100
            angularLeft = self.findAngular(predictions[0][21:24], predictions[0][15:18], predictions[0][33:36]) * 100
            if angularLeft >= 100 or angularRight >= 100:
                count.append(i)
        return count, len(predictions)

    def testcountHand(self, image):
        image = Image.open(image) # If you want to use path can uncommend it
        predictions = self.predictKeypoints(image)
        image = np.asarray(image)
        handUp, countPerson = self.countHand(predictions)
        for idx in handUp:
            plot_skeleton_kpts(image, predictions[idx].T, 3)
        image = Image.fromarray(image)
        return len(handUp), image, countPerson
        

    def countObject(self, predictions, targetClass):
        objectCounts = {targetClass: 0}
        for prediction in predictions:
            if prediction["class"] == targetClass:
                objectCounts[targetClass] += 1
        return objectCounts

    def testobjectDetection(self, imgPath, targetClass):
        predictions = objectModel.predict(f"{imgPath}")
        classCounts = self.countObject(predictions, targetClass)
        return classCounts[targetClass], predictions

    def open_image(self, imgPath):
        # open method used to open different extension image file
        im = Image.open(imgPath) 
        
        # This method will show image in any image viewer 
        im.show()
        return
    
    def count_hand(self):
        # print("Done")
        # self.clear()
        # start_time = time.time()
        
        #Cound Hand Function
        # imgPathHand = r"backup\test5people_hand_up.jpg"
        imgPathHand = r"backup\test5people_hand_down.jpg"
        
        # cam_port = 0
        # cam = cv2.VideoCapture(cam_port)
        # result, image = cam.read()
            
        countHandResult, countedImg, countPerson = self.testcountHand(imgPathHand)
        # countHandResult, countedImg, countPerson = self.testcountHand(image)
        print("Hand Up: ", countHandResult)
        # print("Person: ", countPerson)
        # countedImg.show()
        # print(time.time() - start_time)
        return countHandResult
    
    def count_people(self):
        # print("Done")
        self.clear()
        # start_time = time.time()
        
        #Cound people Function
        imgPathPeople = r"backup\test5people.jpg"
        
        # cam_port = 0
        # cam = cv2.VideoCapture(cam_port)
        # result, image = cam.read()
            
        countHandResult, countedImg, countPerson = self.testcountHand(imgPathPeople)
        # countHandResult, countedImg, countPerson = self.testcountHand(image)
        print("Person: ", countPerson)
        # countedImg.show()
        # print(time.time() - start_time)
        return countPerson

    def count_vote(self):
        
        # count down
        # self.clear()
        # start_time = time.time()
            
        #Object Detection Function
        tagetClass_success = "success"
        tagetClass_fail = "fail"
        
        # for already image
        # imgPathObj = r"backup\4success_1fail.jpg"
        imgPathObj = r"backup\5success.jpg"
        
        # for img from webcam
        # cam_port = 0
        # cam = cv2.VideoCapture(cam_port)
        # result, image = cam.read()
        # cv2.imwrite("vote_temp_img.png", image)
        # imgPathObj = "vote_temp_img.png"
        
        objectDetectresult, resultsJson = self.testobjectDetection(imgPathObj, tagetClass_fail)
        print(f"Number Of Objects [{tagetClass_fail}]:", objectDetectresult)
        # self.open_image(imgPathObj) # show image
            
            # result
        # print(resultsJson)
        # print(time.time() - start_time)
        time.sleep(5)
        return objectDetectresult