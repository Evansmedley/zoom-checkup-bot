# program to capture single image from webcam in python 
  
# importing OpenCV library 
import cv2 as cv 
  
# initialize the camera 
# If you have multiple camera connected with  
# current device, assign a value in cam_port  
# variable according to that 
cam_port = 0
cam = cv.VideoCapture(cam_port) 

for count in range(100):
    # reading the input using the camera 
    result, image = cam.read() 
    

    if result:     # saving image in local storage 
        cv.imwrite("imagesForCalibration/image" + str(count) + ".png", image) 
    
    # If captured image is corrupted, moving to else part 
    else: 
        print("No image detected. Please! try again")
        