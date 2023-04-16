from detectionFunction import objectDetection, delete
from counthandFunction import predictKeypoints, countHand
from utils.plots import plot_skeleton_kpts
from roboflow import Roboflow
from PIL import Image
import numpy as np

def countObject(predictions, targetClass):
    objectCounts = {targetClass: 0}
    for prediction in predictions:
        if prediction["class"] == targetClass:
            objectCounts[targetClass] += 1
    return objectCounts

def testobjectDetection(imgPath,targetClass):
    rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
    project = rf.workspace().project("yolov5-avalon")
    model = project.version(3).model
    predictions = model.predict(f"{imgPath}")
    classCounts = countObject(predictions, targetClass)
    return classCounts[targetClass], predictions

def testcountHand(path):
    image = Image.open(path)
    pred = predictKeypoints(image)
    image = np.asarray(image)
    handUp = countHand(pred)
    for idx in handUp:
        plot_skeleton_kpts(image, pred[idx].T, 3)
    image = Image.fromarray(image)
    return len(handUp), image

#Object Detection Function
imgPathObj = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/backup/IMG_6153.JPG"
objectDetectresult, resultsJson = testobjectDetection(imgPathObj, "success")
print("Number Of Objects: ", objectDetectresult)
print(resultsJson)

#Cound Hand Function
imgPathHand = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/backup/test5.jpg"
countHandResult, countedImg = testcountHand(imgPathHand)
print("Hand Up: ", countHandResult)
countedImg.show()

"""Use in detectionFunction.py
path2Folder = "assets/captureIMG"
objectDetectResult = objectDetection(path2Folder, "Vote", "success", 1)
print("Number Of Objects: ", objectDetectResult)
delete(path2Folder)"""