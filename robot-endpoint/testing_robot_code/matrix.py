from visual_kinematics.RobotSerial import *
from visual_kinematics.RobotTrajectory import *
import numpy as np
from math import pi

def main():
    np.set_printoptions(precision=3, suppress=True)
    # # Length of each link * 10
    MUL = 3
    l0 = 0.061 * MUL  # base to servo 1
    l1 = 0.0435 * MUL # servo 1 to servo 2
    l2 = 0.08285  * MUL# servo 2 to servo 3
    l3 = 0.08285 * MUL # servo 3 to servo 4
    l4 = 0.07385 * MUL # servo 4 to servo 5
    l5 = 0.05457 * MUL # servo 5 to gripper
    # dh_parameters = [
    #     # alpha, a, d, theta
    #     [0, 0, l0, 0],   # Base to servo 1
    #     [90, 0, l1, 0],             # Servo 1 to servo 2
    #     [0, l2, 0, 0],            # Servo 2 to servo 3
    #     [0, l3, 0, 0],            # Servo 3 to servo 4
    #     [-90, l4, 0, 0],            # Servo 4 to servo 5
    #     [0, 0, l5, 0]   # Servo 5 to gripper
    # ]
    #d, a , alpha, theta
    # dh_params = np.array(
    #                   [[l0, 0., 0., 0.],
    #                   [l1, 0., pi / 2 , 0.],
    #                   [0., l2, 0., 0.],
    #                   [0., l3, 0., 0.],
    #                   [0., l4, -pi /2, 0.],
    #                   [l5, 0., 0., 0.]])
    
    dh_params = np.array(
                      [
                      [l0 + l1, 0., pi / 2, 0.],
                      [0., l2, 0., 1.57],
                      [0., l3, 0., 0.],
                      [0., l4 + l5 , 0., 0.]])
    
    

    robot = RobotSerial(dh_params)

    # =====================================
    # forward
    # =====================================

    # theta = np.array([0. - (0.5*pi), 0.- (0.5*pi), 0.- (0.5*pi), 0.- (0.5*pi), 0.- (0.5*pi), 0.- (0.5*pi)])
    theta = np.array([0., 0., 0., 0.])
    f = robot.forward(theta)

    print("-------forward-------")
    print("end frame t_4_4:")
    print(f.t_4_4)
    print("end frame xyz:")
    print(f.t_3_1.reshape([3, ]))
    print("end frame abc:")
    print(f.euler_3)
    print("end frame rotational matrix:")
    print(f.r_3_3)
    print("end frame quaternion:")
    print(f.q_4)
    print("end frame angle-axis:")
    print(f.r_3)

    robot.show()


if __name__ == "__main__":
    main()