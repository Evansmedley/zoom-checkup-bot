import cv2
class ObjectDetect:
    def find_mouth(self, img):
        """Finds the mouth and draws a bounding box
        """
        pass
    
    def find_ulnar_nerve(self, img):
        """Finds the ulnar name and draws bounding box
        """
        pass

class ObjectGrab:

    def flashlight(self, button: bool):
        """Turns on and off the flashlight

        The flashlight is mounted on the top of the robot through GPIO pin
        """
        # TODO: test it in the ubuntu enviornment

        if button:
            # turn on GPIO PIN
            pass
        else:
            # turn off GPIO pin
            pass

    def tongue_depressor(self):
        """Picks up tounge depressor
        """
        pass
    
    def mallet(self):
        """Pick up mallet
        """
        pass


