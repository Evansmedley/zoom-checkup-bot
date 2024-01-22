from Arm_Lib import Arm_Device
import threading
import os
import time
from movements import set_all_angles, BotActions

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

    angle1, angle2, angle3, angle4, angle5, angle6 = set_all_angles()
    move_bot = BotActions(Arm, angle1, angle2, angle3, angle4, angle5, angle6)

    while True:
        req = recieve_request()
        if not req:
            pass
        if "reset" == req:
            move_bot.reset_motors()
        elif "open_claw" == req:
            move_bot.open_claw()
        elif "close_claw" == req:
            move_bot.close_claw()
        elif "turn_right" == req:
            move_bot.turn_right()
        elif "turn_left" == req:
            move_bot.turn_left()
        elif "move_forwards" == req:
            move_bot.move_forwards()
        elif "move_backwards" == req:
            move_bot.move_backwards()
        elif "exit" == req:
            break
    # th1 = threading.Thread(target=move_bot)
    # th1.setDaemon(True)
    # th1.start()

    del Arm