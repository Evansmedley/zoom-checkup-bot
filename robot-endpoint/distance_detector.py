import cv2

class DistanceDetector:

    def __init__(self, ref_image, known_distance, known_width, detector) -> None:
        self._ref_image = ref_image
        self._known_distance = known_distance
        self._known_width = known_width
        self._detector = detector
    
    # focal length finder function 
    def focal_length_finder(self, measured_distance, real_width, width_in_rf_image): 
        focal_length = (width_in_rf_image * measured_distance) / real_width 
        return focal_length 

    # distance estimation function 
    def distance_finder(self, focal_length, face_width_in_frame): 
        distance = (self._known_width * focal_length) / face_width_in_frame 
        return distance
    
    def get_focal_length(self) -> float:
            # reading reference_image from directory 
        ref_image = cv2.imread(self._ref_image) 

        # converting color image to gray scale image 
        gray_image = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY) 
    
        # detecting face in the image 
        faces = self._detector.detectMultiScale(gray_image, 1.3, 5) 

        ref_image_face_width = 0
    
        # looping through the faces detect in the  
        # image getting coordinates x, y , 
        # width and height 
        for (x, y, h, w) in faces: 
    
            # draw the rectangle on the face 
            cv2.rectangle(ref_image, (x, y), (x+w, y+h), (0, 255, 0), 2) 
    
            # getting face width in the pixels 
            ref_image_face_width = w 
        
        focal_length_found = self.focal_length_finder( 
            self._known_distance, self._known_width, ref_image_face_width)
        
        return focal_length_found