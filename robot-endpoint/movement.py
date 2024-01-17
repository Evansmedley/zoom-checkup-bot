import time
import threading
from Arm_Lib import Arm_Device
import cv2
import numpy as np

Arm = Arm_Device()
time.sleep(.1)

def robot_start():
    '''
    Robot init
    '''
    # Alert patient with buzzer
    b_time = 1
    Arm.Arm_Buzzer_On(b_time)
    time.sleep(1)
    # Closed buzzer
    Arm.Arm_Buzzer_Off()
    time.sleep(1)

    # Set to default position
    Arm.Arm_serial_servo_write(1, 0, 100)
    time.sleep(0.1)
    Arm.Arm_serial_servo_write(2, 90, 100)
    time.sleep(0.1)
    Arm.Arm_serial_servo_write(3, 90, 100)
    time.sleep(0.1)
    # upright is 90; pointing away from board is 0; pointing towards board is 180... do not do -90
    Arm.Arm_serial_servo_write(4, 90, 100) 
    time.sleep(0.1)
    # claw twists to face away from LED at 0; forwards at 90; towards LED at 180
    Arm.Arm_serial_servo_write(5, 90, 100)
    time.sleep(0.1)
    # 0 is claw fully open; 165 is safety max
    Arm.Arm_serial_servo_write(6, 90, 500) 
    time.sleep(0.1)

robot_start()

# Control the left and right movement of the No. 1 servo -- not working
Arm.Arm_serial_servo_write(1, 180, 500)
time.sleep(.5)
Arm.Arm_serial_servo_write(1, 0, 1000)
time.sleep(1)

# Stops arm
del Arm