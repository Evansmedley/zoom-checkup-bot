from Arm_Lib import Arm_Device
import threading
import time
from movements import set_all_angles, BotActions

if __name__ == "__main__":

    Arm = Arm_Device()
    time.sleep(.1)

    angle1, angle2, angle3, angle4, angle5, angle6 = set_all_angles()
    move_bot = BotActions(Arm, angle1, angle2, angle3, angle4, angle5, angle6)
    
    th1 = threading.Thread(target=move_bot)
    th1.setDaemon(True)
    th1.start()

    del Arm