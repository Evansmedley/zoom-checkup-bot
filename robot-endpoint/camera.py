import cv2
 
class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
        self.video.set(cv2.CAP_PROP_BRIGHTNESS, 30) 
        self.video.set(cv2.CAP_PROP_CONTRAST, 50) 
        self.video.set(cv2.CAP_PROP_EXPOSURE, 156) 
        self.video.set(3, 640)
        self.video.set(4, 480)
        self.video.set(5, 30)  # set frame
 
    def __del__(self):
        self.video.release()
 
    def get_frame(self):
        success, image = self.video.read()
        if(success == False):
            print ("Read Error!")
            return bytes({1})
        return image