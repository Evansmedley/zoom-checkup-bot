from Arm_Lib import Arm_Device
import threading
import os
import time
from movements import set_all_angles, Move_Motors

PI_IP = "192.68.123.68"

def control():

    Arm = Arm_Device()
    time.sleep(.1)

    motor1, motor2, motor3, motor4, motor5, motor6 = set_all_angles()
    move_bot = Move_Motors(Arm, motor1, motor2, motor3, motor4, motor5, motor6)

    move_bot.reset_motors()
    while True:
        motor_num, angle = receive_request()
        if motor_num is None and angle is None:
            pass
        else:
            move_bot.set_motor(angle, motor_num)
        motor_num, angle = None, None
        
    # th1 = threading.Thread(target=move_bot)
    # th1.setDaemon(True)
    # th1.start()

    del Arm