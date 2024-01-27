import logging
from flask import Flask, request

arm = None

try:
    from control_robot import Arm
    arm = Arm()
except:
    print("test")

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)


@app.post('/liveness')
def liveness_probe():
    app.logger.debug(f'Received liveness probe')
    if app.config.get('uuid') != request.json['uuid']:
        return {"message": "Bad Request, invalid uuid"}, 400
    else:
        return {'uuid': app.config.get('uuid')}


@app.post('/changeArm')
def change_arm():
    app.logger.debug(f'Received request to change arm with value \'{request.json["arm"]}\'')
    
    # If debug mode is not on, select active motor
    if not app.config.get('debug'):
        arm.set_active_motor(request.json['arm'])
    
    return ""
        
@app.post('/changeSlider')
def change_slider():
    app.logger.debug(f'Received request to change slider with value \'{request.json["move"]}\'')
    
    # If debug mode is not on, instruct the robotic arm to move
    if not app.config.get('debug'):
        arm.move(request.json['move'])
    
    return ""