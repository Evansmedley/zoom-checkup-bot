'''
Main Code for the Robotic Arm
'''

import time
from Arm_Lib import Arm_Device

# Create Robot Arm Object
Arm = Arm_Device()
time.sleep(.1)

def RGB_light():
    '''
    LED Light sequence
    '''
    # Run LED setup Sequence
    Arm.Arm_RGB_set(100, 100, 50) #RGB light on
    time.sleep(0.5)

    # Run TX sequence
    Arm.Arm_RGB_set(100, 100, 0) # RGB Red light on
    time.sleep(0.5)

    # Run RX sequence
    Arm.Arm_RGB_set(242, 10, 180) # RGB pink light on
    time.sleep(0.5)


# all movements are with reference to the robot's inital position

def move_right():
    '''
    Moves robot to the right
    '''
    pass

def move_left():
    '''
    Moves robot to left
    '''
    pass

def move_forward():
    '''
    Move robot forwards
    ''' 
    pass

def move_backwards():
    '''
    Move robot retract the robot
    ''' 
    pass

def move_up():
    '''
    Move robot forwards
    ''' 
    pass

def move_down():
    '''
    Move robot forwards
    ''' 
    pass

