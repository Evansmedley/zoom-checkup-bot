import cv2
import ipywidgets.widgets as widgets
import threading
import time
import numpy as np
import enum
import cv2
import matplotlib.pyplot as plt

def face_filter(faces):

    if len(faces) == 0: return None

    max_face = max(faces, key=lambda face: face[2] * face[3])
    (x, y, w, h) = max_face

    if w < 10 or h < 10: return None
    return max_face
    

def follow_function(img):
    img = cv2.resize(img, (640, 480))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.copy()
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    if len(faces) != 0:
        face = face_filter(faces)

        (x, y, w, h) = face

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
        cv2.putText(img, 'Person', (280, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (105, 105, 105), 2)
        point_x = x + w / 2
        point_y = y + h / 2
    return img
    
def face_enhancer():
    #Picture whitening formula：p = P*1.4(a)+ b;\n",

"img = cv2.imread('yahboom.jpg',1),
"imgInfo = img.shape\n",
"height = imgInfo[0]\n",
"width = imgInfo[1]\n",
"#cv2.imshow('src',img)\n",
"dst = np.zeros((height,width,3),np.uint8)\n",
"for i in range(0,height):\n",
"    for j in range(0,width):\n",
"        (b,g,r) = img[i,j]\n",
"        bb = int(b*1.3) + 10\n",
"        gg = int(g*1.2) + 15\n",
"\n",
"        if bb>255:\n",
"            bb = 255\n",
"        if gg>255:\n",
"            gg = 255\n",
"\n",
"        dst[i,j] = (bb,gg,r)\n",
"# cv2.imshow('dst',dst)\n",
"# cv2.waitKey(0)\n",
"img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
"dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)\n",
"plt.figure(figsize=(14, 6), dpi=100) #Set the size and pixels of the drawing area\n",
"plt.subplot(121)  #The first in a row and two columns\n",
"plt.imshow(img)\n",
"plt.subplot(122)  #The second in a row and two columns\n",
"plt.imshow(dst)\n",
"plt.show()"
faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)

width=600
height=500
try:
    while True:
        ret, frame = image.read()
        img = follow_function(frame)
        cv2.imshow("Camera Stream", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break # wait until a key is pressed
except KeyboardInterrupt:
    print(" Program closed!")
    pass

image.release()
cv2.destroyAllWindows()
