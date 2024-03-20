# import numpy as np

# # Lengths of each link
# l0 = 0.061   # base to servo 1
# l1 = 0.0435  # servo 1 to servo 2
# l2 = 0.08285 # servo 2 to servo 3
# l3 = 0.08285 # servo 3 to servo 4
# l4 = 0.07385 # servo 4 to servo 5
# l5 = 0.05457 # servo 5 to gripper

# # Angles in degrees (90, 90, 90, 90, 90, 0)
# theta = np.radians([90, 90, 90, 90, 90, 0])

# # Forward kinematics function
# def forward_kinematics(theta):
#     x = l0 * np.cos(theta[0]) + l1 * np.cos(theta[0] + theta[1]) + \
#         l2 * np.cos(theta[0] + theta[1] + theta[2]) + \
#         l3 * np.cos(theta[0] + theta[1] + theta[2] + theta[3]) + \
#         l4 * np.cos(theta[0] + theta[1] + theta[2] + theta[3] + theta[4]) + \
#         l5 * np.cos(theta[0] + theta[1] + theta[2] + theta[3] + theta[4] + theta[5])

#     y = l0 * np.sin(theta[0]) + l1 * np.sin(theta[0] + theta[1]) + \
#         l2 * np.sin(theta[0] + theta[1] + theta[2]) + \
#         l3 * np.sin(theta[0] + theta[1] + theta[2] + theta[3]) + \
#         l4 * np.sin(theta[0] + theta[1] + theta[2] + theta[3] + theta[4]) + \
#         l5 * np.sin(theta[0] + theta[1] + theta[2] + theta[3] + theta[4] + theta[5])

#     return x, y

# # Check if any joint goes below the base
# x, y = forward_kinematics(theta)
# if y < 0:
#     print("One of the joints goes below the base, adjusting angles...")
#     # Adjusting the angles to prevent joints from going below the base
#     theta[0] = np.pi / 2  # Keeping the base vertical
#     theta[4] = 0  # Keeping joint 5 vertical
#     for i in range(1, len(theta)-1):  # Loop through all but the last angle
#         if theta[i] < 0:
#             theta[i] = 0  # Preventing negative angles

#     x, y = forward_kinematics(theta)
#     print("Adjusted angles:", np.degrees(theta))
#     print("Final position:", (x, y))
# else:
#     print("All joints are above the base.")

from Arm_Lib import Arm_Device
import numpy as np

arm = Arm_Device()

# Lengths of each link
l0 = 0.061   # base to servo 1
l1 = 0.0435  # servo 1 to servo 2
l2 = 0.08285 # servo 2 to servo 3
l3 = 0.08285 # servo 3 to servo 4
l4 = 0.07385 # servo 4 to servo 5
l5 = 0.05457 # servo 5 to gripper

# Angles in degrees (90, 90, 90, 90, 90, 0)
angles = [90, 90, 90, 90, 90, 0]
theta = np.radians(angles)

# Forward kinematics function
def forward_kinematics(theta):
    x = l0 * np.cos(theta[0]) + l1 * np.cos(theta[0] + theta[1]) + \
        l2 * np.cos(theta[0] + theta[1] + theta[2]) + \
        l3 * np.cos(theta[0] + theta[1] + theta[2] + theta[3]) + \
        l4 * np.cos(theta[0] + theta[1] + theta[2] + theta[3] + theta[4])

    y = l0 * np.sin(theta[0]) + l1 * np.sin(theta[0] + theta[1]) + \
        l2 * np.sin(theta[0] + theta[1] + theta[2]) + \
        l3 * np.sin(theta[0] + theta[1] + theta[2] + theta[3]) + \
        l4 * np.sin(theta[0] + theta[1] + theta[2] + theta[3] + theta[4])

    return x, y

# Check if any joint goes below the base
x, y = forward_kinematics(theta)
if y < 0:
    print("One of the joints goes below the base, adjusting angles...")
    # Adjusting the angles to prevent joints from going below the base
    theta[0] = np.pi / 2  # Keeping the base vertical
    for i in range(1, len(theta)-1):  # Loop through all but the last angle
        if theta[i] < 0:
            theta[i] = 0  # Preventing negative angles

    x, y = forward_kinematics(theta)
    print("Adjusted angles:", np.degrees(theta))
    print("Final position:", (x, y))
else:
    print("All joints are above the base.")
    arm.Arm_serial_servo_write6(angles[0], angles[1], angles[2], angles[3], angles[4], angles[5], 500)

del arm
