import cv2 as cv
import threading
from time import sleep
import ipywidgets as widgets
from IPython.display import display

cam = cv.VideoCapture(0)

class RobotAuto:

    def find_mouth(self, img):
        """Finds the mouth and draws a bounding box
        """
        pass
    
    def find_funny_bone(self, img):
        """Finds the ulnar name and draws bounding box
        """
        pass

    def flashlight(self, button: bool):
        """Turns on and off the flashlight
        """
        pass

def camera_start():
    cam = cv.VideoCapture(0)
    while cam.isOpened():
        try:
            ret, img = cam.read()
            img = cv.resize(img, (640, 480))
        except KeyboardInterrupt:cam.release()


camera_start()



