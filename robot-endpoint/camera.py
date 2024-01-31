import cv2
import ipywidgets.widgets as widgets
import threading
import time
import numpy as np
import enum
import cv2
import matplotlib.pyplot as plt
import distance_detector

def face_filter(faces):

    if len(faces) == 0: return None

    max_face = max(faces, key=lambda face: face[2] * face[3])
    (x, y, w, h) = max_face

    if w < 10 or h < 10: return None
    return max_face

def follow_function(img, focal_length):
    img = cv2.resize(img, (640, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.copy()
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) != 0:
        face = face_filter(faces)

        (x, y, w, h) = face

        distance_to_camera = distanceDetect.distance_finder(focal_length, w)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.putText(img, 'Person', (280, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (105, 105, 105), 2)
        cv2.putText(img, 'Distance ' + str(distance_to_camera), (280, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (105, 105, 105), 2)
        point_x = x + w / 2
        point_y = y + h / 2
    return img

faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)

# For Jeremy's Testing
#image = cv2.VideoCapture(0)

width=600
height=500

try:
    distanceDetect = distance_detector.DistanceDetector("Ref_image.jpg", 65, 17, faceDetect)
    focal_length = distanceDetect.get_focal_length()

    while True:
        ret, frame = image.read()
        img = follow_function(frame, focal_length)
        cv2.imshow("Camera Stream", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break # wait until a key is pressed
except KeyboardInterrupt:
    print(" Program closed!")
    pass

image.release()
cv2.destroyAllWindows()
