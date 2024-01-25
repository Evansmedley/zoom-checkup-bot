import cv2

class MouthDetector:
    def __init__(self, mouth_cascade_path):
        # Load the pre-trained mouth cascade classifier
        self.mouth_cascade = cv2.CascadeClassifier(mouth_cascade_path)

        # Open a connection to the camera (usually 0 or 1 for built-in cameras)
        self.cap = cv2.VideoCapture(0)

    def detect(self):
        while True:
            # Read a frame from the camera
            ret, frame = self.cap.read()

            # Convert the frame to grayscale for mouth detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect mouths in the grayscale frame
            mouths = self.mouth_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (mx, my, mw, mh) in mouths:
                # Extract the region around the mouth
                mouth_roi = frame[my:my+mh, mx:mx+mw]

                # Display the region
                cv2.imshow('Mouth Region', mouth_roi)

                # Draw rectangle around the mouth
                cv2.rectangle(frame, (mx, my), (mx+mw, my+mh), (0, 255, 0), 2)

            # Display the frame
            cv2.imshow('Video', frame)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close the windows
        self.cap.release()
        cv2.destroyAllWindows()

# Path to the Haar Cascade XML file for mouth detection
# TODO: Create haarcascade_mouth.xml 
mouth_cascade_path = cv2.data.haarcascades + 'haarcascade_mouth.xml'

# Create an instance of the MouthDetector class
mouth_detector = MouthDetector(mouth_cascade_path)

# Start mouth detection
mouth_detector.detect()
