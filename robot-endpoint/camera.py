import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import ipywidgets.widgets as widgets

def bgr8_to_jpeg(value, quality=75):
    return bytes(cv2.imencode('.jpg', value)[1])

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

# camera widget
image_widget = widgets.Image(format='jpeg', width=600, height=500) 

