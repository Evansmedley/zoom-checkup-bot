import threading
import os
import time
from movements import set_all_angles, Move_Motors
from Arm_Lib import Arm_Device


PI_IP = "192.68.123.68"

class Arm():
    
    def __init__(self):
        self.arm = Arm_Device()
        self.move_bot = self.setup()
        self.active_motor_num = None
        
        
    def setup(self):
        time.sleep(.1)

        motor1, motor2, motor3, motor4, motor5, motor6 = set_all_angles()
        move_bot = Move_Motors(self.arm, motor1, motor2, motor3, motor4, motor5, motor6)

        move_bot.reset_motors()
        
        return move_bot


    def move(self, angle: int):
        if self.active_motor_num is None and angle is None:
            pass
        else:
            self.move_bot.set_motor(angle, self.active_motor_num)
        angle = None
        
    
    def set_active_motor(self, motor_num: int):
        self.active_motor_num = motor_num
    
    
    def cleanup():
        del Arm

    # NOT SURE WHAT TO DO WITH THIS :)        
    # th1 = threading.Thread(target=move_bot)
    # th1.setDaemon(True)
    # th1.start()
