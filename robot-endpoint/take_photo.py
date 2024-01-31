import cv2

cam = cv2.VideoCapture(0, cv2.CAP_GSTREAMER)

while True:
    ret, frame = cam.read()
    cv2.imshow("Image", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Ref_image.jpg", frame)
        break;


