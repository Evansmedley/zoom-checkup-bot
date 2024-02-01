import numpy as np
from utils import rot, get_homogeneous, R2rpy
from Robot import UR5Arm


def fwdkin(arm: UR5Arm, theta: np.array) -> tuple():
    """Calculates the forward kinematics of the DofBot
    Args:
        arm - Robot arm class with home config info and joint value
        theta - (5 x 1) the angles of rotation for each joint
    Returns:
        R - a numpy array with shape (3,3)
        P - a numpy array with shape (3,)
    """
    P = arm.get_P()
    H = arm.get_H()

    R_0T = np.eye(3)
    P_0T = P[:, 0]

    for i in range(1, P.shape[1]):
        R_ij = rot(H[:, i - 1], theta[i - 1, 0])

        R_0T = R_0T @ R_ij
        P_0T = P_0T + R_0T @ P[:, i]
    H = get_homogeneous(R_0T, P_0T.reshape(3, 1))

    return H[0:3, 0:3], H[:3, 3]


def invkin(arm: UR5Arm, Rd, Pd, q0=np.array([50,50,50,50,50])[None].T*np.pi/180, max_iters=2000, alpha=0.1, tol=1e-4):
    """Calculates the inverse kinematics of a 
    Args:
        Arm - Robot arm class with end effector home config info and 
            current joint values
        Rd - the desired Rotation of EE
        Pd - the desired Positon of EE
        q0 - (5x1) the initial guess joint configuration
        max_iters - maximum number of gradient steps
        tol - convergence criteria
    """
    assert (q0.shape == (5, 1))
    q_prev = q0
    q_cur = q0

    iter = 0
    converged = np.array([False] * 5)
    while iter < max_iters and not converged.all():

        # get the homogenous transform of current q
        R_cur, P_cur = fwdkin(arm, q_cur)
        # get the postion and Orientation

        if iter == 0: print(R_cur, P_cur)

        P_err = P_cur - Pd
        R_err = R_cur @ Rd.T
        # calculate r
        r = np.array(R2rpy(R_err))

        J0T = arm.jacobian(q_cur)
        # computer the update value
        err = np.concatenate((r.T, P_err))

        converged = np.absolute(err) <= tol
        if converged.all():
            print(err)
            print(f"Inverse Kinematics Converged after {iter} iterations")
            return True, q_cur

        j = np.linalg.pinv(J0T) @ err
        q_cur = q_prev - alpha * j.reshape(5, 1)
        q_prev = q_cur

        iter += 1

    print("Inverse Kinematics Didn't Converge")
    return False, q_cur