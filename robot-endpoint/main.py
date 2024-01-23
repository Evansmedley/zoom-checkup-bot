from Arm_Lib import Arm_Device
import threading
import os
import time
from movements import set_all_angles, Move_Motors

PI_IP = "192.68.123.68"

def recieve_request() -> str:
    """ Recieve a request from the website
    """
    # TODO: Get the request from the website button press
    pass

def get_current_IP():
    """Taken from the DOFBOT repo

    Returns:
        _type_: _description_
    """
    ip = os.popen("/sbin/ifconfig eth0 | grep 'inet' | awk '{print $2}'").read()
    ip = ip[0 : ip.find('\n')]
    if(ip == ''):
        #Read WLAN IP
        ip = os.popen("/sbin/ifconfig wlan0 | grep 'inet' | awk '{print $2}'").read()
        ip = ip[0 : ip.find('\n')]
        if(ip == ''):
            ip = 'x.x.x.x'
    return ip

if __name__ == "__main__":

    Arm = Arm_Device()
    time.sleep(.1)

    motor1, motor2, motor3, motor4, motor5, motor6 = set_all_angles()
    move_bot = Move_Motors(Arm, motor1, motor2, motor3, motor4, motor5, motor6)

    move_bot.reset_motors()
    while True:
        motor_num, angle = recieve_request()
        if motor_num is None and angle is None:
            pass
        else:
            move_bot.set_motor(angle, motor_num)
        motor_num, angle = None, None
        
    # th1 = threading.Thread(target=move_bot)
    # th1.setDaemon(True)
    # th1.start()

    del Arm