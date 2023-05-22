import time
from roboflow import Roboflow
import cv2, os

rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
# project = rf.workspace().project("yolov5-avalon-scoretableau")
project = rf.workspace().project("yolov5-avalon")
model = project.version(4).model

x=0
camera = cv2.VideoCapture(1)
while True:
    ret, frame = camera.read()
    cv2.imshow('frame', frame)
    if x >= 150:
        cv2.imwrite(os.path.join("C:\Prab\Year 2\Cognitive computer\Board-Games-Assistant-Year2-Semester2\capturePic", 'capturedPicture.jpg'), frame)
        print(model.predict("C:\Prab\Year 2\Cognitive computer\Board-Games-Assistant-Year2-Semester2\capturePic\capturedPicture.jpg", confidence=40, overlap=30).json())
        break
    x+=1

camera.release()
cv2.destroyAllWindows()