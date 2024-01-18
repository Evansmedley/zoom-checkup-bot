import time
import threading
from Arm_Lib import Arm_Device
# import cv2
import numpy as np
from dataclasses import dataclass

MOVEMENT_TIME = 100
STEP_ANGLE = 1

Arm = Arm_Device()
time.sleep(.1)

@dataclass
class MotorAngle:
    motor_id: int
    min_angle: int
    max_angle: int
    curr_angle: float
    time_run: int

angle1 = MotorAngle(1, 0, 180, 0, MOVEMENT_TIME)
angle2 = MotorAngle(2, 0, 180, 90, MOVEMENT_TIME)
angle3 = MotorAngle(3, 0, 180, 90, MOVEMENT_TIME)
angle4 = MotorAngle(4, 0, 180, 90, MOVEMENT_TIME)
angle5 = MotorAngle(5, 0, 180, 90, MOVEMENT_TIME)
angle6 = MotorAngle(6, 0, 165, 90, 500)

def reset_robot():
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
    Arm.Arm_serial_servo_write6(0, 90, 90, 90, 90, 90, 500)
    time.sleep(1)
    return

def move_bot(key_press: str) -> None:
    """Moves robot based on key press

    Args:
        key_press (str): user input key
    """
    def boundaries(next_angle: float, angle_num: MotorAngle) -> MotorAngle:
        """ Forces the robot to stay within the boundaries

        Args:
            next_angle (float): desired angle for motor
            angle_num (MotorAngle): data class containing all the information about the motor

        Returns:
            MotorAngle: recalculated motor angle data class
        """
        if angle_num.max_angle <= next_angle:
            angle_num.curr_angle = angle_num.max_angle
        elif angle_num.min_angle >= next_angle:
            angle_num.curr_angle = angle_num.min_angle
        else:
            angle_num.curr_angle = next_angle
        return angle_num
    
    # left and right controlled by Motor 1 (keys A and D)
    # large range up and down controlled by Motor 2 (keys W and S)
    # medium range up and down controlled by Motor 3 (keys R and F)
    # small range up and down controlled by Motor 4 (keys I and K)
    # swivel of claw controlled by Motor 5 (keys left and right)
    # opening of claw controlled by Motor 6 (keys up and down)
    # space bar to reset to default position

    if key_press == "space_bar":
        time.sleep(5)
        reset_robot()

    key_dict = {
        'A': (angle1, STEP_ANGLE),
        'D': (angle1, 0-STEP_ANGLE),
        'W': (angle2, STEP_ANGLE),
        'S': (angle2, 0-STEP_ANGLE),
        'R': (angle3, STEP_ANGLE),
        'F': (angle3, 0-STEP_ANGLE),
        'I': (angle4, STEP_ANGLE),
        'K': (angle4, 0-STEP_ANGLE),
        'left': (angle5, STEP_ANGLE),
        'right': (angle5, 0-STEP_ANGLE),
        'up': (angle6, STEP_ANGLE),
        'down': (angle6, 0-STEP_ANGLE),
    }

    key_value = key_dict.get(key_press)
    motor_angle, new_step_angle = key_value

    motor_angle = boundaries(motor_angle.curr_angle + new_step_angle, motor_angle)
    Arm.Arm_serial_servo_write(motor_angle.motor_id, motor_angle.curr_angle, motor_angle.time_run)
    time.sleep(0.01)

def grab_tool():
    pass


if __name__ == "__main__":
    reset_robot()
    th1 = threading.Thread(target=move_bot)
    th1.setDaemon(True)
    th1.start()

    # need to add a error handler

    # Stops arm
    del Arm