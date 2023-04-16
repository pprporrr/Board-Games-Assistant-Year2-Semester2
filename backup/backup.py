import os
import cv2
import time
from roboflow import Roboflow


def objectDetection(apiKey, projectName, versionNumber, targetClass, captureDevice=1):
    rf = Roboflow(api_key=apiKey)
    project = rf.workspace().project(projectName)
    model = project.version(versionNumber).model
    cap = cv2.VideoCapture(captureDevice)

    imgCounter = 0
    path = 'assets/captureIMG'

    def countObject(predictions, target_class):
        object_counts = {target_class: 0}
        for prediction in predictions:
            if prediction['class'] == target_class:
                object_counts[target_class] += 1
        return object_counts

    def captureWebcam():
        ret, frame = cap.read()
        if not ret:
            print("Error: could not read frame from video stream")
            return
        imgName = f'{targetClass}_{imgCounter}.png'
        cv2.imwrite(os.path.join(path, imgName), frame)
        predictions = model.predict(f'{path}/{imgName}')
        classCounts = countObject(predictions, targetClass)
        successCount = classCounts[targetClass]
        print(successCount)
        print('\n')

    # set the start time
    startTime = time.time()

    while True:
        captureWebcam()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # check if 10 seconds have passed
        elapsedTime = time.time() - startTime
        if elapsedTime > 10:
            break

    cap.release()
    cv2.destroyAllWindows()


objectDetection("szKo1b01Oo737AK9Apzk", "yolov5-avalon", 3, 'success')
