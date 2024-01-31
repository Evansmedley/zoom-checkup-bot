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

        self.a = [1, 1, 1, 1, 1, 1] # link length
        self.d = [0, 0, 0, 0, 0, 0] # translation
        self.main()

    def transformation_matrix(self, i: int) -> list:
        """Returns a transformation matrix as a list oflists

        Args:
            i (int): end of link i to the base of link i

        Returns:
            list: Transformation matrix for joint i
        """
        t_m = [[m.cos(self.theta[i-1]), -1 * m.sin(self.theta[i-1]) * m.cos(self.alpha[i-1]), m.sin(self.theta[i-1]) * m.sin(self.alpha[i-1]), self.a[i-1]*m.cos(self.theta[i-1])],
            [m.sin(self.theta[i-1]), m.cos(self.theta[i-1])*m.cos(self.alpha[i-1]), -1 * m.cos(self.theta[i-1])*m.sin(self.alpha[i-1]), self.a[i-1]*m.sin(self.theta[i-1])],
            [0, m.sin(self.alpha[i-1]), m.cos(self.alpha[i-1]), self.d[i-1]],
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
        print("MATRIX LIST[i]:", i)
        pprint.pprint(matrix_list[i])
        current_matrix = np.matmul(current_matrix, matrix_list[i])
        print("CURRENT MATRIX:", i)
        pprint.pprint(current_matrix)
        return self.multiply_matrices(i=i+1, matrix_list=matrix_list, current_matrix=current_matrix)

    def main(self):
        """Print and run the matrix operations
        """
        matrix_list = []
        for i in range(1,7):
            matrix_list.append(np.array(self.transformation_matrix(i)))
        pprint.pprint(matrix_list)
        pprint.pprint(self.multiply_matrices(i=1, matrix_list=matrix_list, current_matrix=matrix_list[0]))
        
#Test values
fwd_k = ForwardKinematics([90, 90, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0])


