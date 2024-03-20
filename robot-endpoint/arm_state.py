
class ArmState:
    
    MOTOR_LIMITS = {1: (0, 180),
                    2: (0, 180),
                    3: (0, 180),
                    4: (0, 180),
                    5: (0, 270),
                    6: (0, 180)}
    
    def __init__(self):
        self.motor_angles = [self.MOTOR_LIMITS[i+1][1] // 2 for i in range(6)]
        self.active_motor_num = 1
        
    def set_motor_angle(self, angle: int) -> None:
        self.motor_angles[self.active_motor_num- 1] = angle
        
    def get_motor_angle(self, motor_num: int) -> int:
        self.active_motor_num = motor_num
        return self.motor_angles[motor_num - 1]
    