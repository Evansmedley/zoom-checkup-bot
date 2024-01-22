import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


# import cv2
# import ipywidgets.widgets as widgets
# import threading
# import time
# import enum

# image_widget = widgets.Image(format='jpeg', width=600, height=500)
# display(image_widget) # Display camera widget

# def bgr8_to_jpeg(value, quality=75):
#     """
#     bgr8 to jpeg converter
#     """
#     return bytes(cv2.imencode('.jpg', value)[1])

# image = cv2.VideoCapture(0)                           

# width=600
# height=500
# ret, frame = image.read()    
# image_widget.value = bgr8_to_jpeg(frame)

# try:
#     while 1:
#         ret, frame = image.read()
#         image_widget.value = bgr8_to_jpeg(frame)
#         time.sleep(0.010)
# except KeyboardInterrupt:
#     print(" Program closed! ")
#     pass

# image.release() 