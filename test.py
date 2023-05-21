from roboflow import Roboflow

rf = Roboflow(api_key="szKo1b01Oo737AK9Apzk")
project = rf.workspace().project("yolov5-avalon-scoretableau")
model = project.version(1).model

# infer on a local image
print(model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/backup/Tableau10.JPG", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("/Users/ppr/Desktop/Project/Board-Games-Assistant-Year2-Semester2/backup/Tableau10.JPG", confidence=40, overlap=30).save("Tableau10_prediction_2.JPG")