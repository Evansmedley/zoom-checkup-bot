import math as m
import numpy as np
import pprint

def convert_to_rad(degrees_list: list) -> list:
    """Convert from degrees to radians

    Args:
        degrees_list (list): list of degrees

    Returns:
        list: list of radians
    """
    rad_list = []
    for i in degrees_list:
        rad_list.append(m.radians(i))

    return rad_list

def Dofbot_Params():
    # all revolute joints
    l0 = 0.061 # base to servo 1 in meters
    l1 = 0.0435 # servo 1 to servo 2
    l2 = 0.08285 # servo 2 to servo 3
    l3 = 0.08285 # servo 3 to servo 4
    l4 = 0.07385 # servo 4 to servo 5 
    l5 = 0.05457 # servo 5 to gripper

    # Identity matrix
    ex = np.array([1, 0, 0])
    ey = np.array([0, 1, 0])
    ez = np.array([0, 0, 1])

    P01 = ( l0 + l1 ) * ez # translation between 0 and 1 frame in 0 frame
    P12 = np.zeros (3) # translation between 1 and 2 frame in 1 frame
    P23 = l2 * ex # translation between 2 and 3 frame in 2 frame
    P34 = - l3 * ez # translation between 3 and 4 frame in 3 frame
    P45 = np.zeros (3) # translation between 4 and 5 frame in 4 frame
    P5T = -( l4 + l5 ) * ex 
    
    # Translation
    print("Translation")
    print(P01, P12, P23, P34, P45, P5T)

    DofbotP = np.array([P01, P12, P23, P34, P45, P5T]).T
    pprint.pprint(DofbotP)
    DofbotH = np.array([ez, -ey, -ey, -ey, -ex]).T
    pprint.pprint(DofbotH)

class ForwardKinematics:
    """Finds position of end effector based on the current joint positions
    """
    def __init__(self, theta_list:list, alpha_list:list) -> None:
        """Init for ForwardKinematics

        Args:
            theta_list (list): Xi/Xi-1 about Zi-1 angle in degrees
            alpha_list (list): Zi/Zi-1 about Xi
        """
        self.theta = convert_to_rad(theta_list) # angle of each axis in degrees
        self.alpha = convert_to_rad(alpha_list)# zero for a planar manipulator
        l0 = 0.061 # base to servo 1
        l1 = 0.0435 # servo 1 to servo 2
        l2 = 0.08285 # servo 2 to servo 3
        l3 = 0.08285 # servo 3 to servo 4
        l4 = 0.07385 # servo 4 to servo 5
        l5 = 0.05457 # servo 5 to gripper

        self.a = [0, 0, 0, 0, l4, 0] # link length in meters
        self.d = [l0, l1, l2, l3, 0, l5] # translation
        self.main()

    def transformation_matrix(self, i: int) -> list:
        """Returns a transformation matrix as a list oflists

        Args:
            i (int): end of link i to the base of link i

        Returns:
            list: Transformation matrix for joint i
        """
        t_m = [[int(m.cos(self.theta[i-1])), int(-1 * m.sin(self.theta[i-1]) * m.cos(self.alpha[i-1])),int( m.sin(self.theta[i-1]) * m.sin(self.alpha[i-1])), int(self.a[i-1]*m.cos(self.theta[i-1]))],
            [int(m.sin(self.theta[i-1])), int(m.cos(self.theta[i-1])*m.cos(self.alpha[i-1])), int(-1 * m.cos(self.theta[i-1])*m.sin(self.alpha[i-1])), int(self.a[i-1]*m.sin(self.theta[i-1]))],
            [0, int(m.sin(self.alpha[i-1])), int(m.cos(self.alpha[i-1])), int(self.d[i-1])],
            [0, 0, 0, 1]]
        return t_m
    
    def multiply_matrices(self, i:int, matrix_list:list, current_matrix: np.array) -> np.array:
        """Find transformation matrix for the end effector relative to the base

        Args:
            i (int): matriz number
            matrix_list (list): list of matrices
            current_matrix (np.array): matrix computed

        Returns:
            np.array: ^0_6T transformation matrix
        """
        if i == len(matrix_list):
            return current_matrix
        # print("MATRIX LIST[i]:", i)
        # pprint.pprint(matrix_list[i])
        current_matrix = np.matmul(current_matrix, matrix_list[i])
        # print("CURRENT MATRIX:", i)
        # pprint.pprint(current_matrix)
        return self.multiply_matrices(i=i+1, matrix_list=matrix_list, current_matrix=current_matrix)

    def main(self):
        """Print and run the matrix operations
        """
        matrix_list = []
        for i in range(1,7):
            matrix_list.append(np.array(self.transformation_matrix(i)))
        # pprint.pprint(matrix_list)
        print("FINAL VALUES")
        pprint.pprint(self.multiply_matrices(i=1, matrix_list=matrix_list, current_matrix=matrix_list[0]))
        
#Test values
fwd_k = ForwardKinematics([90, 90, 0, 0, 0, 0], [0, 0, 0, 0, 90, 0])
# print(f_)
print("DOFBOT")
# Dofbot_Params()

