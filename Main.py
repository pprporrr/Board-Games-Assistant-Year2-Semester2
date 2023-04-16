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

def testobjectDetection(targetClass):
    rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
    project = rf.workspace().project("yolov5-avalon")
    model = project.version(3).model
    predictions = model.predict("/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/backup/IMG_6153.JPG")
    classCounts = countObject(predictions, targetClass)
    return classCounts[targetClass], predictions

result, resultsJson = testobjectDetection("success")

print("objectCount: ", result)
print(resultsJson)

#path2Folder = "assets/captureIMG"

#result = objectDetection(path2Folder, "success", 1)

#delete(path2Folder)

IMAGEFILE = "/Users/ppr/Desktop/Project/2_2 BOARDGAMESASSISTANT/backup/test5.jpg"
image = Image.open(IMAGEFILE)
pred = predictKeypoints(image)
image = np.asarray(image)
handUp = countHand(pred)
print("handCount: ", len(handUp))
for idx in handUp:
    plot_skeleton_kpts(image, pred[idx].T, 3)
image = Image.fromarray(image)
image.show()