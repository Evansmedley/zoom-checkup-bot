from Arm_Lib import Arm_Device

arm = Arm_Device()
arm.Arm_serial_servo_write6(80, 90, 90, 0, 90, 165, 500)
del arm