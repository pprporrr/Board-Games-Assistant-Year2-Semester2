import os, cv2, time, shutil
from roboflow import Roboflow

def delete(path2Folder):
    for fileName in os.listdir(path2Folder):
        filePath = os.path.join(path2Folder, fileName)
        try:
            if os.path.isfile(filePath) or os.path.islink(filePath):
                os.unlink(filePath)
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath)
        except Exception as e:
            pass

def objectDetection(path2Folder, state, targetClass, imgCounter, captureDevice = 0):
    if (state == "Init"):
        rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
        project = rf.workspace().project("yolov5-avalon-score")
        model = project.version(1).model
        cap = cv2.VideoCapture(captureDevice)
    elif (state == "Vote"):
        rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
        project = rf.workspace().project("yolov5-avalon")
        model = project.version(3).model
        cap = cv2.VideoCapture(captureDevice)

    def countObject(predictions, targetClass):
        objectCounts = {targetClass: 0}
        for prediction in predictions:
            if prediction["class"] == targetClass:
                objectCounts[targetClass] += 1
        return objectCounts

    def captureWebcam():
        ret, frame = cap.read()
        if not ret:
            print("Error: could not read frame from video stream")
            return
        imgName = f"{state}_{imgCounter}.png"
        cv2.imwrite(os.path.join(path2Folder, imgName), frame)
        predictions = model.predict(f'{path2Folder}/{imgName}')
        classCounts = countObject(predictions, targetClass)
        return classCounts[targetClass]

    for i in range(10, 0, -1):
        print("Countdown:", i)
        time.sleep(1)
    print("objectDetection!")
    classCounts = captureWebcam()
    
    cap.release()
    cv2.destroyAllWindows()
    
    return classCounts