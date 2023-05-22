import time
from roboflow import Roboflow
import cv2

rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon-scoretableau")
model = project.version(1).model

cap = cv2.VideoCapture(0)

for i in range(5, 0, -1):
    print(f"Capturing picture in {i} seconds...")
    time.sleep(1)

ret, frame = cap.read()

if ret:
    cv2.imshow('Virtual Webcam', frame)
    cv2.imwrite('captured_picture.jpg', frame)
    print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/IMG_6554.JPG", confidence=40, overlap=30).json())
    print("\n")
    print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/IMG_6555.JPG", confidence=40, overlap=30).json())
    print("\n")
    print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/IMG_6557.JPG", confidence=40, overlap=30).json())
    print("\n")
    print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/IMG_6558.JPG", confidence=40, overlap=30).json())
    print("\n")
    print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/IMG_6559.JPG", confidence=40, overlap=30).json())
    print("\n")
    print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/IMG_6561.JPG", confidence=40, overlap=30).json())
else:
    print("Failed to capture frame")

cap.release()
cv2.destroyAllWindows()