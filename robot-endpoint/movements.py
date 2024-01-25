import time
import threading
from Arm_Lib import Arm_Device
from dataclasses import dataclass

MOVEMENT_TIME = 1000
# Tested constraints manually

limits = {
    [90, 180, 90, 90, 90, 90], # flat back DO NOT MOVE 3, 4 below 90
    [90, 0, 90, 60, 90, 90],  # lowest forward with motor 2 at 0
    [90, 50, 0, 60, 90, 90],  # lowest forward with motor 3 at 0
}

@dataclass
class Motors:
    motor_id: int
    min_angle: int
    max_angle: int
    curr_angle: int
    time_run: int

class Move_Motors:
    def __init__(self, Arm, motor1, motor2, motor3, motor4, motor5, motor6) -> None:
        self.Arm = Arm
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4
        self.motor5 = motor5
        self.motor6 = motor6

        self.motor_dict = {
            1: self.motor1,
            2: self.motor2,
            3: self.motor3,
            4: self.motor4,
            5: self.motor5,
            6: self.motor6
        }

        self.reset_motors()
    
    def reset_motors(self) -> None:
        """ 
        Resets all motor angles after a delay of 3 seconds
        """
        time.sleep(1)
        # buzzer_time = 1 # Alert with buzzer
        # self.Arm.Arm_Buzzer_On(buzzer_time)
        # time.sleep(1)

        # # Closed buzzer
        # self.Arm.Arm_Buzzer_Off()
        # time.sleep(1)

        # Set to default position
        self.Arm.Arm_serial_servo_write6(90, 90, 90, 0, 90, 165, 500)
        time.sleep(1)

    def boundaries(self, next_angle: int, motor: Motors) -> int:
        """ Forces the robot to stay within the boundaries

        Args:
            next_angle (float): desired angle for motor
            angle_num (MotorAngle): data class containing all the information about the motor

        Returns:
            MotorAngle: recalculated motor angle data class
        """
        if motor.max_angle <= next_angle:
            motor.curr_angle = motor.max_angle
        elif motor.min_angle >= next_angle:
            motor.curr_angle = motor.min_angle
        else:
            motor.curr_angle = next_angle
        return motor.curr_angle
    
    def update_real_position(self) -> list:
        """
        Updates the location of all motor angles
        """
        self.motor1.curr_angle = self.Arm.Arm_serial_servo_read(self.motor1.motor_id)
        self.motor2.curr_angle = self.Arm.Arm_serial_servo_read(self.motor2.motor_id)
        self.motor3.curr_angle = self.Arm.Arm_serial_servo_read(self.motor3.motor_id)
        self.motor4.curr_angle = self.Arm.Arm_serial_servo_read(self.motor4.motor_id)
        self.motor5.curr_angle = self.Arm.Arm_serial_servo_read(self.motor5.motor_id)
        self.motor6.curr_angle = self.Arm.Arm_serial_servo_read(self.motor6.motor_id)
    

    def set_motor(self, angle: int, motor_num: int) -> None:
        """
        Sets the position of the angle for each motor

        Args:
            motor_int (int): motor number to set
            angle (int): angle to set
        """
        motor = self.motor_dict[motor_num]
        new_angle = self.boundaries(angle, motor)
        delta_t = self.time_duration(angle, new_angle)
        self.Arm.Arm_serial_servo_write(motor.motor_id, new_angle, motor.time_run)
        time.sleep(delta_t+0.01)
        self.update_real_position()
    
    def time_duration(self, current_angle:int, final_angle:int) -> float:
        """Time to move the robot

        Args:
            current_angle (int): current angle
            final_angle (int): destination angle

        Returns:
            float: time taken
        """
        # for 90 degrees it takes 1 second
        time_per_angle = 1/90
        return abs(final_angle - current_angle) * time_per_angle

def set_all_angles():
    motor1 = Move_Motors(1, 0, 180, 90, MOVEMENT_TIME)
    motor2 = Move_Motors(2, 0, 130, 90, MOVEMENT_TIME)
    motor3 = Move_Motors(3, 0, 180, 90, MOVEMENT_TIME)
    motor4 = Move_Motors(4, -40, 180, 0, MOVEMENT_TIME)
    motor5 = Move_Motors(5, 0, 180, 90, MOVEMENT_TIME)
    motor6 = Move_Motors(6, 0, 165, 165, 500)

    return motor1, motor2, motor3, motor4, motor5, motor6