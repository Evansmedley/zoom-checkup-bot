import time
import threading
from Arm_Lib import Arm_Device
from dataclasses import dataclass

MOVEMENT_TIME = 100
STEP_ANGLE = 15
STEP_ANGLE_MOV = 10

@dataclass
class MotorAngle:
    motor_id: int
    min_angle: int
    max_angle: int
    curr_angle: int
    time_run: int

class BotActions:
    """Bot Action Class
    """
    def __init__(self, Arm, angle1, angle2, angle3, angle4, angle5, angle6) -> None:
        self.Arm = Arm
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        self.angle4 = angle4
        self.angle5 = angle5
        self.angle6 = angle6

        self.reset_motors()

    def boundaries(self, next_angle: float, angle_num: MotorAngle) -> MotorAngle:
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
        return angle_num.curr_angle
    
    def reset_motors(self) -> None:
        """ 
        Resets all motor angles after a delay of 3 seconds
        """
        time.sleep(3)
        buzzer_time = 1 # Alert with buzzer
        self.Arm.Arm_Buzzer_On(buzzer_time)
        time.sleep(1)

        # Closed buzzer
        self.Arm.Arm_Buzzer_Off()
        time.sleep(1)

        # Set to default position
        self.Arm.Arm_serial_servo_write6(0, 90, 90, 90, 90, 90, 500)
        time.sleep(1)

        self.update_position()

    def update_position(self) -> None:
        """
        Updates the location of all motor angles
        """
        self.angle1.curr_angle = self.Arm.Arm_serial_servo_read(self.angle1.motor_id)
        self.angle2.curr_angle = self.Arm.Arm_serial_servo_read(self.angle2.motor_id)
        self.angle3.curr_angle = self.Arm.Arm_serial_servo_read(self.angle3.motor_id)
        self.angle4.curr_angle = self.Arm.Arm_serial_servo_read(self.angle4.motor_id)
        self.angle5.curr_angle = self.Arm.Arm_serial_servo_read(self.angle5.motor_id)
        self.angle6.curr_angle = self.Arm.Arm_serial_servo_read(self.angle6.motor_id)

    def set_motor(self, motor: MotorAngle, ang: int) -> None:
        """
        Sets the position of the angle for each motor

        Args:
            motor (MotorAngle): motor to set
            ang (int): angle to set
        """
        self.Arm.Arm_serial_servo_write(motor.motor_id, ang, motor.time_run)
        time.sleep(0.5)
        self.update_position()

    def open_claw(self) -> None:
        """
        Opens end effector
        """
        self.set_motor(self.angle6.motor_id, self.angle6.max_angle)
    
    def close_claw(self) -> None:
        """
        Closes end effector
        """
        motor_angle = self.boundaries(self.angle6.curr_angle + STEP_ANGLE, self.angle6)
        self.set_motor(self.angle6, motor_angle)
    
    def turn_right(self) -> None:
        """
        Turns robot right
        """
        motor_angle = self.boundaries(self.angle1.curr_angle - STEP_ANGLE_MOV, self.angle1)
        self.set_motor(self.angle1, motor_angle)
    
    def turn_left(self) -> None:
        """
        Turns robot left
        """
        motor_angle = self.boundaries(self.angle1.curr_angle + STEP_ANGLE_MOV, self.angle1)
        self.set_motor(self.angle1, motor_angle)

    def move_forwards(self) -> None:
        """
        Moves robot forward
        """
        # TODO: change move forwards so end effector remains parallel with the table when moving
        self.angle2.curr_angle = 90
        self.angle3.curr_angle = 0
        self.angle4.curr_angle = 90

        self.set_motor(self.angle2, self.angle2.curr_angle)
        self.set_motor(self.angle3, self.angle3.curr_angle)
        self.set_motor(self.angle4, self.angle4.curr_angle)

    def move_backwards(self) -> None:
        """
        Moves Robot backwards
        """
        # TODO: change move backwards so end effector remains parallel with the table when moving
        self.set_motor(self.angle2, self.angle2.curr_angle)
        self.set_motor(self.angle3, self.angle3.curr_angle)
        self.set_motor(self.angle4, self.angle4.curr_angle)

def set_all_angles():
    angle1 = MotorAngle(1, 0, 180, 0, MOVEMENT_TIME)
    angle2 = MotorAngle(2, 0, 180, 90, MOVEMENT_TIME)
    angle3 = MotorAngle(3, 0, 180, 90, MOVEMENT_TIME)
    angle4 = MotorAngle(4, 0, 180, 90, MOVEMENT_TIME)
    angle5 = MotorAngle(5, 0, 180, 90, MOVEMENT_TIME)
    angle6 = MotorAngle(6, 0, 165, 90, 500)

    return angle1, angle2, angle3, angle4, angle5, angle6