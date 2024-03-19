from Arm_Lib import Arm_Device
import numpy as np
from Robot import UR5Arm
import time

rarm = Arm_Device()
def set_angles(arm, angles, sec_per_angle):
    """Sets all the angles of arm
    Args:
        arm - the real robot
        angles - the angles to set
        t - the amount of time to move each angle
    """
    angles = (angles * 180/np.pi).astype(int)
    print("here", angles)
    t = angles*sec_per_angle
    for joint, (angle, movetime) in enumerate(zip(angles, t)):
        time.sleep(1)
        print(f"Command: Joint {joint+1} -> {angle} deg in {movetime} ms")
        arm.Arm_serial_servo_write(joint+1, angle, movetime)
        time.sleep(1)
        
def read_all_joints_in_radians(arm):
    q = np.array([arm.Arm_serial_servo_read(id) for id in range(1,6)])*np.pi/180
    return q
rarm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 165, 500)

l0 = 0.061 # base to servo 1
l1 = 0.0435 # servo 1 to servo 2
l2 = 0.08285 # servo 2 to servo 3
l3 = 0.08285 # servo 3 to servo 4
l4 = 0.07385 # servo 4 to servo 5
l5 = 0.05457 # servo 5 to gripper

ex = np.array([1,0,0])
ey = np.array([0,1,0])
ez = np.array([0,0,1])

P01 = ( l0 + l1 ) * ez 
P12 = np.zeros (3) # translation between 1 and 2 frame in 1 frame
P23 = l2 * ex # translation between 2 and 3 frame in 2 frame
P34 = - l3 * ez # translation between 3 and 4 frame in 3 frame
P45 = np.zeros (3) # translation between 4 and 5 frame in 4 frame
P5T = -( l4 + l5 ) * ex 
print(P01,P12,P23,P34,P45,P5T)

P = np.array([P01, P12, P23, P34, P45, P5T]).T
H = np.array([ez, -ey, -ey, -ey, -ex]).T
limits = np.array([0,180] * 6).reshape(6, 2)
limits[4, :] = [0, 270]
print(f"limits: \n{limits}")
del rarm