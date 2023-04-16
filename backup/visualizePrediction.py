from re import T
from roboflow import Roboflow
rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon")
model = project.version(3).model

# infer on a local image
#print(model.predict("IMG_6153.JPG", confidence=40, overlap=30).json())

# visualize your prediction
number = 6153
while True:
    model.predict("IMG_{}.JPG".format(number), confidence=40, overlap=30).save("IMG_{}_prediction.jpg".format(number))
    if number == 6160:
        break
    number += 1

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())