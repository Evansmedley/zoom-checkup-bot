# Robot Controller
## Yahboom Control

## Inverse Kinematics

## Grabbing Objects

## Object Identification

## Dependancies


## Running script
To prevent conflicts with native Yahboom App run every time on the Raspberry Pi
sh ~/Dofbot/kill_YahboomArm.sh

To run the script locally without a robotic arm present use:
python3 main.py -n {NAME} -s 127.0.0.1 -p {LISTEN_PORT} -d -l

To run the script locally with a robotic arm present use:
python3 main.py -n {NAME} -s 127.0.0.1 -p {LISTEN_PORT} -l

To run the script using the cloud server without a robotic arm present use:
python3 main.py -n {NAME} -s {SERVER_IP} -p {LISTEN_PORT} -d

To run the script using the cloud server with a robotic arm present use:
python3 main.py -n {NAME} -s {SERVER_IP} -p {LISTEN_PORT}
