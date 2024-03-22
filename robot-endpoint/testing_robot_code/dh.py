
# import math

# # # Length of each link
# l0 = 0.064  # base to servo 1
# l1 = 0.0435  # servo 1 to servo 2
# l2 = 0.08285  # servo 2 to servo 3
# l3 = 0.08285  # servo 3 to servo 4
# l4 = 0.07385  # servo 4 to servo 5
# l5 = 0.05457  # servo 5 to gripper ?????
# print(l0 + l1 + l2 + l3 + l4 + l5)

# # DH parameters for the robotic arm
# dh_parameters = [
#     # alpha, a, d, theta
#     [0, 0, l0, 0],   # Base to servo 1
#     [90, 0, l1, 0],             # Servo 1 to servo 2
#     [0, l2, 0, 0],            # Servo 2 to servo 3
#     [0, l3, 0, 0],            # Servo 3 to servo 4
#     [-90, l4, 0, 0],            # Servo 4 to servo 5
#     [0, 0, l5, 0]   # Servo 5 to gripper
# ]

# # Convert degrees to radians for joint angles
# for i in range(len(dh_parameters)):
#     dh_parameters[i][3] = math.radians(dh_parameters[i][3] - 90 )
#     dh_parameters[i][0] = math.radians(dh_parameters[i][1])

# # Function to calculate transformation matrix for DH parameters
# def dh_transform(alpha, a, d, theta):
#     return [
#         [math.cos(theta), -math.sin(theta) * math.cos(alpha), math.sin(theta) * math.sin(alpha), a * math.cos(theta)],
#         [math.sin(theta), math.cos(theta) * math.cos(alpha), -math.cos(theta) * math.sin(alpha), a * math.sin(theta)],
#         [0, math.sin(alpha), math.cos(alpha), d],
#         [0, 0, 0, 1]
#     ]

# # Function to calculate end effector position using DH parameters
# def calculate_end_effector_position(angles):
#     transform = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
#     for i in range(len(dh_parameters)):
#         alpha, a, d, theta = dh_parameters[i]
#         theta += angles[i]
#         transform_i = dh_transform(alpha, a, d, theta)
#         transform = [[sum(a * b for a, b in zip(row, col)) for col in zip(*transform_i)] for row in transform]
#     return transform[0][3], transform[1][3], transform[2][3]

# # Check if any joint goes below the base
# def check_below_base(angles):
#     x, y, z = calculate_end_effector_position(angles)
#     print("x: ", x, "y: ", y, "z: ", z)
#     if z < 0:
#         return True
#     return False

# # Home position angles (degrees)
# # NEVER CHANGE FIRST VALUE
# angles = [0, 0, 0, 0, 0, 0]

# # Test
# if check_below_base(angles):
#     print("Robot arm goes below the base!")
# else:
#     print("Robot arm stays above the base.")



# import numpy as np
# l0 = 0.064  # base to servo 1
# l1 = 0.0435  # servo 1 to servo 2
# l2 = 0.08285  # servo 2 to servo 3
# l3 = 0.08285  # servo 3 to servo 4
# l4 = 0.07385  # servo 4 to servo 5
# l5 = 0.05457  # servo 5 to gripper ?????
# def dh_matrix(alpha, a, d, theta):
#     """
#     Calculate DH transformation matrix
#     """
#     return np.array([
#         [np.cos(theta),               -np.sin(theta),               0,               a],
#         [np.sin(theta)*np.cos(alpha), np.cos(theta)*np.cos(alpha), -np.sin(alpha), -np.sin(alpha)*d],
#         [np.sin(theta)*np.sin(alpha), np.cos(theta)*np.sin(alpha),  np.cos(alpha),  np.cos(alpha)*d],
#         [0,                            0,                            0,               1]
#     ])

# def forward_kinematics(dh_table):
#     """
#     Calculate the forward kinematics
#     """
#     T = np.eye(4)  # Identity matrix to start with
    
#     for dh_row in dh_table:
#         alpha, a, d, theta = dh_row
#         theta = np.radians(theta - 90)
#         alpha = np.radians(alpha)
#         print(dh_matrix(alpha, a, d, theta))
#         T = np.dot(T, dh_matrix(alpha, a, d, theta))
    
#     return T

# # DH parameters for the robotic arm
# dh_parameters = [
#     # alpha, a, d, theta
#     [0, 0, l0, 0],   # Base to servo 1
#     [90, 0, l1, 0],             # Servo 1 to servo 2
#     [0, l2, 0, 0],            # Servo 2 to servo 3
#     [0, l3, 0, 0],            # Servo 3 to servo 4
#     [-90, l4, 0, 0],            # Servo 4 to servo 5
#     [0, 0, l5, 0]   # Servo 5 to gripper
# ]

# # Calculate forward kinematics
# result = forward_kinematics(dh_parameters)

# # Extract the position and orientation
# position = result[:3, 3]
# orientation = result[:3, :3]

# print("Forward Kinematics Result:")
# print("Position:", position)
# print("Orientation:")
# print(orientation)


import numpy as np # Scientific computing library
 
# Project: Coding Denavit-Hartenberg Tables Using Python - 6DOF Robotic Arm
#          This code excludes the servo motor that controls the gripper.
# Author: Addison Sears-Collins
# Date created: August 22, 2020
 
# Link lengths in centimeters

# l0 = 0.064  # base to servo 1
# l1 = 0.0435  # servo 1 to servo 2
# l2 = 0.08285  # servo 2 to servo 3
# l3 = 0.08285  # servo 3 to servo 4
# l4 = 0.07385  # servo 4 to servo 5
# l5 = 0.05457  # servo 5 to gripper ?????
a1 = 6.4 # Length of link 1
a2 = 4.35 # Length of link 2
a3 = 8.285 # Length of link 3
a4 = 8.285 # Length of link 4
a5 = 7.385 # Length of link 5
a6 = 5.457 # Length of link 6
 
# Initialize values for the joint angles (degrees)
theta_1 = 0 - 90 # Joint 1
theta_2 = 0 - 90  # Joint 2
theta_3 = 0 - 90 # Joint 3
theta_4 = 0 - 90 # Joint 4
theta_5 = 0 - 90 # Joint 5
 
# Declare the Denavit-Hartenberg table. 
# It will have four columns, to represent:
# theta, alpha, r, and d
# We have the convert angles to radians.
d_h_table = np.array([[np.deg2rad(theta_1), np.deg2rad(90), 0, a1],
                      [np.deg2rad(theta_2), 0, a2, 0],
                      [np.deg2rad(theta_3), 0, a3, 0],
                      [np.deg2rad(theta_4 + 90), np.deg2rad(90), a5,0],
                      [np.deg2rad(theta_5), 0, 0, a4 + a6]]) 
 
# Homogeneous transformation matrix from frame 0 to frame 1
i = 0
homgen_0_1 = np.array([[np.cos(d_h_table[i,0]), -np.sin(d_h_table[i,0]) * np.cos(d_h_table[i,1]), np.sin(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.cos(d_h_table[i,0])],
                      [np.sin(d_h_table[i,0]), np.cos(d_h_table[i,0]) * np.cos(d_h_table[i,1]), -np.cos(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.sin(d_h_table[i,0])],
                      [0, np.sin(d_h_table[i,1]), np.cos(d_h_table[i,1]), d_h_table[i,3]],
                      [0, 0, 0, 1]])  
 
# Homogeneous transformation matrix from frame 1 to frame 2
i = 1
homgen_1_2 = np.array([[np.cos(d_h_table[i,0]), -np.sin(d_h_table[i,0]) * np.cos(d_h_table[i,1]), np.sin(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.cos(d_h_table[i,0])],
                      [np.sin(d_h_table[i,0]), np.cos(d_h_table[i,0]) * np.cos(d_h_table[i,1]), -np.cos(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.sin(d_h_table[i,0])],
                      [0, np.sin(d_h_table[i,1]), np.cos(d_h_table[i,1]), d_h_table[i,3]],
                      [0, 0, 0, 1]])  
 
# Homogeneous transformation matrix from frame 2 to frame 3
i = 2
homgen_2_3 = np.array([[np.cos(d_h_table[i,0]), -np.sin(d_h_table[i,0]) * np.cos(d_h_table[i,1]), np.sin(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.cos(d_h_table[i,0])],
                      [np.sin(d_h_table[i,0]), np.cos(d_h_table[i,0]) * np.cos(d_h_table[i,1]), -np.cos(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.sin(d_h_table[i,0])],
                      [0, np.sin(d_h_table[i,1]), np.cos(d_h_table[i,1]), d_h_table[i,3]],
                      [0, 0, 0, 1]])  
 
# Homogeneous transformation matrix from frame 3 to frame 4
i = 3
homgen_3_4 = np.array([[np.cos(d_h_table[i,0]), -np.sin(d_h_table[i,0]) * np.cos(d_h_table[i,1]), np.sin(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.cos(d_h_table[i,0])],
                      [np.sin(d_h_table[i,0]), np.cos(d_h_table[i,0]) * np.cos(d_h_table[i,1]), -np.cos(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.sin(d_h_table[i,0])],
                      [0, np.sin(d_h_table[i,1]), np.cos(d_h_table[i,1]), d_h_table[i,3]],
                      [0, 0, 0, 1]])  
 
# Homogeneous transformation matrix from frame 4 to frame 5
i = 4
homgen_4_5 = np.array([[np.cos(d_h_table[i,0]), -np.sin(d_h_table[i,0]) * np.cos(d_h_table[i,1]), np.sin(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.cos(d_h_table[i,0])],
                      [np.sin(d_h_table[i,0]), np.cos(d_h_table[i,0]) * np.cos(d_h_table[i,1]), -np.cos(d_h_table[i,0]) * np.sin(d_h_table[i,1]), d_h_table[i,2] * np.sin(d_h_table[i,0])],
                      [0, np.sin(d_h_table[i,1]), np.cos(d_h_table[i,1]), d_h_table[i,3]],
                      [0, 0, 0, 1]])  
 
homgen_0_5 = homgen_0_1 @ homgen_1_2 @ homgen_2_3 @ homgen_3_4 @ homgen_4_5 
 
# Print the homogeneous transformation matrices
print("Homogeneous Matrix Frame 0 to Frame 5:")
print(homgen_0_5)