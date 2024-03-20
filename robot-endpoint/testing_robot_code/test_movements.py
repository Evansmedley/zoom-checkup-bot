# from Arm_Lib import Arm_Device
# import numpy as np
# from Robot import UR5Arm
# import time

# rarm = Arm_Device()
# def set_angles(arm, angles, sec_per_angle):
#     """Sets all the angles of arm
#     Args:
#         arm - the real robot
#         angles - the angles to set
#         t - the amount of time to move each angle
#     """
#     angles = (angles * 180/np.pi).astype(int)
#     print("here", angles)
#     t = angles*sec_per_angle
#     for joint, (angle, movetime) in enumerate(zip(angles, t)):
#         time.sleep(1)
#         print(f"Command: Joint {joint+1} -> {angle} deg in {movetime} ms")
#         arm.Arm_serial_servo_write(joint+1, angle, movetime)
#         time.sleep(1)
        
# def read_all_joints_in_radians(arm):
#     q = np.array([arm.Arm_serial_servo_read(id) for id in range(1,6)])*np.pi/180
#     return q
# rarm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 165, 500)

# l0 = 0.061 # base to servo 1
# l1 = 0.0435 # servo 1 to servo 2
# l2 = 0.08285 # servo 2 to servo 3
# l3 = 0.08285 # servo 3 to servo 4
# l4 = 0.07385 # servo 4 to servo 5
# l5 = 0.05457 # servo 5 to gripper

# ex = np.array([1,0,0])
# ey = np.array([0,1,0])
# ez = np.array([0,0,1])

# P01 = ( l0 + l1 ) * ez 
# P12 = np.zeros (3) # translation between 1 and 2 frame in 1 frame
# P23 = l2 * ex # translation between 2 and 3 frame in 2 frame
# P34 = - l3 * ez # translation between 3 and 4 frame in 3 frame
# P45 = np.zeros (3) # translation between 4 and 5 frame in 4 frame
# P5T = -( l4 + l5 ) * ex 
# print(P01,P12,P23,P34,P45,P5T)

# P = np.array([P01, P12, P23, P34, P45, P5T]).T
# H = np.array([ez, -ey, -ey, -ey, -ex]).T
# limits = np.array([0,180] * 6).reshape(6, 2)
# limits[4, :] = [0, 270]
# print(f"limits: \n{limits}")
# del rarm


import numpy as np

# Define DH parameters for the robotic arm (example values)
dh_params = [
    [0, 0, 10, 0],    # base_link to shoulder_link
    [0, 0, 10, 0],    # shoulder_link to elbow_link
    [0, 0, 10, 0],    # elbow_link to wrist_link
    [0, 0, 5, 0],     # wrist_link to gripper_link
]

# Define boundaries of the box (example values)
box_boundaries = {
    'x_min': 0,
    'x_max': 50,
    'y_min': 0,
    'y_max': 50,
    'z_min': 0,
    'z_max': 50
}

# Function to check if the end effector is within the boundaries
def within_boundaries(x, y, z):
    return (
        box_boundaries['x_min'] <= x <= box_boundaries['x_max'] and
        box_boundaries['y_min'] <= y <= box_boundaries['y_max'] and
        box_boundaries['z_min'] <= z <= box_boundaries['z_max']
    )

# Function to calculate transformation matrix using DH parameters
def dh_transformation(alpha, a, d, theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)*np.cos(alpha), np.sin(theta)*np.sin(alpha), a*np.cos(theta)],
        [np.sin(theta), np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), a*np.sin(theta)],
        [0, np.sin(alpha), np.cos(alpha), d],
        [0, 0, 0, 1]
    ])

# Function to calculate end effector position based on joint angles
def calculate_end_effector_position(joint_angles):
    # Initialize transformation matrix
    T = np.eye(4)
    
    # Iterate through DH parameters and calculate transformation matrices
    for i, params in enumerate(dh_params):
        alpha, a, d, theta = params
        theta += joint_angles[i]  # Incorporate joint angle
        
        # Calculate transformation matrix for current joint
        T_i = dh_transformation(alpha, a, d, theta)
        
        # Multiply with previous transformation matrix
        T = np.dot(T, T_i)
    
    # Extract end effector position (assuming gripper_link is at the end)
    end_effector_position = T[:3, 3]
    return end_effector_position

# Function to move the arm and check boundaries
def move_arm(joint_angles):
    # Calculate end effector position
    end_effector_position = calculate_end_effector_position(joint_angles)
    
    # Check if end effector is within the boundaries
    if within_boundaries(*end_effector_position):
        print("End effector is within boundaries. Moving arm...")
        # Implement arm movement logic here
    else:
        print("End effector is out of boundaries. Adjusting movement or stopping.")

# Example usage:
joint_angles = [0, 0, 0, 0]  # Example joint angles
move_arm(joint_angles)



#----------------------------------------------------------------




import numpy as np

# Link lengths
l0 = 0.061   # base to servo 1
l1 = 0.0435  # servo 1 to servo 2
l2 = 0.08285 # servo 2 to servo 3
l3 = 0.08285 # servo 3 to servo 4
l4 = 0.07385 # servo 4 to servo 5
l5 = 0.05457 # servo 5 to gripper

# Forward Kinematics function to compute joint positions
def forward_kinematics(theta):
    # Convert angles from degrees to radians
    theta = np.radians(theta)
    
    # Transformation matrices
    T_01 = np.array([[np.cos(theta[0]), -np.sin(theta[0]), 0, 0],
                     [np.sin(theta[0]), np.cos(theta[0]), 0, 0],
                     [0, 0, 1, l0],
                     [0, 0, 0, 1]])

    T_12 = np.array([[np.cos(theta[1]), -np.sin(theta[1]), 0, l1],
                     [0, 0, 1, 0],
                     [-np.sin(theta[1]), -np.cos(theta[1]), 0, 0],
                     [0, 0, 0, 1]])

    T_23 = np.array([[np.cos(theta[2]), -np.sin(theta[2]), 0, l2],
                     [0, 0, 1, 0],
                     [-np.sin(theta[2]), -np.cos(theta[2]), 0, 0],
                     [0, 0, 0, 1]])

    T_34 = np.array([[np.cos(theta[3]), -np.sin(theta[3]), 0, l3],
                     [0, 0, -1, 0],
                     [np.sin(theta[3]), np.cos(theta[3]), 0, 0],
                     [0, 0, 0, 1]])

    T_45 = np.array([[np.cos(theta[4]), -np.sin(theta[4]), 0, l4],
                     [0, 0, -1, 0],
                     [np.sin(theta[4]), np.cos(theta[4]), 0, 0],
                     [0, 0, 0, 1]])

    T_56 = np.array([[np.cos(theta[5]), -np.sin(theta[5]), 0, l5],
                     [np.sin(theta[5]), np.cos(theta[5]), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
    
    # Final transformation matrix
    T_final = T_01 @ T_12 @ T_23 @ T_34 @ T_45 @ T_56
    
    # Extract joint positions
    joint_positions = T_final[:3, 3]
    
    return joint_positions

# Function to check if any joint position is below the base
def check_joint_position(theta):
    joint_positions = forward_kinematics(theta)
    return all(pos[2] >= 0 for pos in joint_positions)

# Example angles
angles = [0, 0, 0, 0, 0, 0]  # initial angles

if not check_joint_position(angles):
    print("Initial joint positions are below the base.")
else:
    print("Initial joint positions are valid.")
