import time
import threading
from Arm_Lib import Arm_Device
from dataclasses import dataclass

MOVEMENT_TIME = 1000
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
    def __init__(self, Arm, motor1, motor2, motor3, motor4, motor5, motor6) -> None:
        self.Arm = Arm
        self.motor1 = motor1
        self.motor2 = motor2
        self.motor3 = motor3
        self.motor4 = motor4
        self.motor5 = motor5
        self.motor6 = motor6

        self.reset_motors()

    def boundaries(self, next_angle: int, angle_num: MotorAngle) -> int:
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

        self.update_position()
  
    def print_position(self) -> None:
        """
        Updates the location of all motor angles
        """
        print(self.motor1.motor_id, self.Arm.Arm_serial_servo_read(self.motor1.motor_id))
        print(self.motor2.motor_id, self.Arm.Arm_serial_servo_read(self.motor2.motor_id))
        print(self.motor3.motor_id, self.Arm.Arm_serial_servo_read(self.motor3.motor_id))
        print(self.motor4.motor_id, self.Arm.Arm_serial_servo_read(self.motor4.motor_id))
        print(self.motor5.motor_id, self.Arm.Arm_serial_servo_read(self.motor5.motor_id))
        print(self.motor6.motor_id, self.Arm.Arm_serial_servo_read(self.motor6.motor_id))

    def update_position(self) -> None:
        """
        Updates the location of all motor angles
        """
        self.motor1.curr_angle = self.Arm.Arm_serial_servo_read(self.motor1.motor_id)
        self.motor2.curr_angle = self.Arm.Arm_serial_servo_read(self.motor2.motor_id)
        self.motor3.curr_angle = self.Arm.Arm_serial_servo_read(self.motor3.motor_id)
        self.motor4.curr_angle = self.Arm.Arm_serial_servo_read(self.motor4.motor_id)
        self.motor5.curr_angle = self.Arm.Arm_serial_servo_read(self.motor5.motor_id)
        self.motor6.curr_angle = self.Arm.Arm_serial_servo_read(self.motor6.motor_id)

    def set_motor(self, motor: MotorAngle, ang: int) -> None:
        """
        Sets the position of the angle for each motor

        Args:
            motor (MotorAngle): motor to set
            ang (int): angle to set
        """
        new_angle = self.boundaries(ang, motor)
        self.Arm.Arm_serial_servo_write(motor.motor_id, new_angle, motor.time_run)

    def open_claw(self) -> None:
        """
        Opens end effector
        """
        self.set_motor(self.motor6.motor_id, self.motor6.max_angle)
    
    def close_claw(self) -> None:
        """
        Closes end effector
        """
        motor_angle = self.boundaries(self.motor6.curr_angle + STEP_ANGLE, self.motor6)
        self.set_motor(self.motor6, motor_angle)
    
    def turn_right(self) -> None:
        """
        Turns robot right
        """
        motor_angle = self.boundaries(self.motor1.curr_angle - STEP_ANGLE_MOV, self.motor1)
        self.set_motor(self.motor1, motor_angle)
    
    def turn_left(self) -> None:
        """
        Turns robot left
        """
        motor_angle = self.boundaries(self.motor1.curr_angle + STEP_ANGLE_MOV, self.motor1)
        self.set_motor(self.motor1, motor_angle)

    def move_forwards(self) -> None:
        """
        Moves robot forward
        """
        if self.motor4.curr_angle < 90:
            self.motor2.curr_angle = self.motor2.curr_angle - 5
            self.motor4.curr_angle = self.motor4.curr_angle + 5
            self.set_motor(self.motor2, self.motor2.curr_angle)
            time.sleep(0.02)
            print(self.motor2.curr_angle)
            self.set_motor(self.motor4, self.motor4.curr_angle)
            time.sleep(0.1)

    def move_backwards(self) -> None:
        """
        Moves Robot backwards
        """
        STEP_ANGLE 
        self.motor2.curr_angle = self.motor2.curr_angle + 5
        self.motor4.curr_angle = self.motor4.curr_angle - 5
        self.set_motor(self.motor2, self.motor2.curr_angle)
        time.sleep(0.02)
        self.set_motor(self.motor4, self.motor4.curr_angle)
        time.sleep(0.1)
        print(self.motor2.curr_angle)
        
    def test_forwards(self):
        self.set_motor(self.motor4, 90)
        time.sleep(0.1)
        t_d = self.time_duration(self.motor2.curr_angle, 0)
        self.set_motor(self.motor2, 0)
        time.sleep(t_d)
#         while self.motor4.curr_angle < 90:
#             self.move_forwards()
        while True:
            try:
                pass
                self.move_backwards()
            except KeyboardInterrupt:
                break
    def robot_constraints(self):
        """ Set so it doesn't slam into the floor"""
        pass

    def time_duration(self, current_angle, final_angle) -> float:
        """Time to move the robot

        Args:
            current_angle (_type_): _description_
            final_angle (_type_): _description_

        Returns:
            float: _description_
        """
        # for 90 degrees it takes 1 second
        time_per_angle = 1/90
        return abs(final_angle - current_angle) * time_per_angle


def set_all_angles():
    motor1 = MotorAngle(1, 0, 180, 90, MOVEMENT_TIME)
    motor2 = MotorAngle(2, 0, 130, 90, MOVEMENT_TIME)
    motor3 = MotorAngle(3, 0, 180, 90, MOVEMENT_TIME)
    motor4 = MotorAngle(4, -40, 180, 0, MOVEMENT_TIME)
    motor5 = MotorAngle(5, 0, 180, 90, MOVEMENT_TIME)
    motor6 = MotorAngle(6, 0, 165, 165, 500)

    return motor1, motor2, motor3, motor4, motor5, motor6