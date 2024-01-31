import cv2
import ipywidgets.widgets as widgets
import threading
import time

import enum
import cv2
    
image = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)

width=600
height=500

i = 0
try:
    while True:
        ret, frame = image.read()
        #image_widget.value = bgr8_to_jpeg(frame)
        
        #cv2.imwrite('img3.jpg', frame)
        #time.sleep(0.010)
        cv2.imshow("Camera Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break # wait until a key is pressed
        
        i += 1
except KeyboardInterrupt:
    print(" Program closed!")
    pass

image.release()
cv2.destroyAllWindows()
