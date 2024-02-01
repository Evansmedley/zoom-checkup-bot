import numpy as np
from utils import rot, hat

class UR5Arm:
    def __init__(self, P, H, limits=None):
        """
        Args: 
            P - 3 x 6 matrix where column i is the position of
                point i to point i+1. (N-1 is the number of joints)
            H - 3 x 5 matrix to denote the axis of rotation of each
                joint in the home configuration.
            limits - joint angle limits
        """
        self.P = P
        self.H = H
        self.L = limits

    def get_P(self):
        """Returns a 3x6 array whose columns contains
        the relative position of joint i to i+1
        """
        return self.P

    def get_H(self):
        """Returns a 3x5 array whose columns constain 
        the axes of rotation of each joint
        """
        return self.H

    def get_Limits(self) -> list:
        """Returns the joint limits in a list of tuples length: 6 (including gripper)
        """
        return self.L

    def get_EE_limits(self):
        
        pass

    def get_PiT(self, jt):
        """Returns a 3x5 matrix of the position of the end effector (T) with respect to 
        joint (i) in the ith frame
        """
        joint_angles = jt
        if joint_angles.shape == (5, 1):
            joint_angles = jt.T

        # assert(joint_angles.shape == (1,5))
        P = self.P
        H = self.H
        R = np.eye(3)
        PiT = np.zeros((3, 6))
        PiT[:, -1] = P[:, -1]
        for i in range(5, 0, -1):
            R = R @ rot(H[:, i - 1], joint_angles[i - 1])
            PiT[:, i] = P[:, i] + R @ PiT[:, i]
        return PiT

    def jacobian(self, jt) -> np.array:
        """Returns the jacobian of this robot arm with joint angles
        """
        joint_angles = np.squeeze(jt.reshape(1, 5))
        # assert (len(joint_angles) == self.H.shape[1], 
        # "number of joint angles is greater than number of non-end-effector joint")
        # The Jacobian is defined as 
        """ 
        # J = [[ h_1,        h_1 x R01 @ P1T                ] 
        #      [ R01 @ h_2,  (R01 @ h_2) x R02 @ P2T        ]
        #      [ .                                          ]
        #      [ .                                          ]
        #      [ .                                          ]
        #      [ R0,N-1 @ h_N,  (R0,N-1 @ h_N) x R0,N @ PNT,]].T
        """
        J = np.zeros((6, 5))
        PiT = self.get_PiT(joint_angles)
        H = self.H
        R = np.eye(3)
        for i in range(len(joint_angles)):
            dw = R @ H[:, i]
            R = R @ rot(H[:, i], joint_angles[i])
            # print(R)
            dv = hat(dw) @ R @ PiT[:, i + 1]
            J[:, i] = np.concatenate((dw.T, dv.T), axis=0).T
        return J