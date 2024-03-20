import logging
from flask import Flask, request, jsonify, Response
from arm_state import ArmState

arm = None

try:
    from control_robot import Arm
    arm = Arm()
except:
    print("test")

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

arm_state = ArmState()


def cors_preflight_response():
    headers = {'Access-Control-Allow-Headers': 'Content-Type, Authorization',
               'Access-Control-Allow-Methods': 'POST'}
    return ('', 204, headers)


@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.post('/liveness')
def liveness_probe():
    app.logger.debug(f'Received liveness probe')
    if app.config.get('uuid') != request.json['uuid']:
        return {"message": "Bad Request, invalid uuid"}, 400
    else:
        return {'uuid': app.config.get('uuid')}


@app.route('/changeArm', methods=['POST', 'OPTIONS'])
def change_arm():
    if request.method == 'OPTIONS':
        return cors_preflight_response()
    
    app.logger.debug(f'Received request to change arm with value \'{request.json["arm"]}\'')
    
    # If debug mode is not on, select active motor
    if not app.config.get('debug'):
        arm.set_active_motor(request.json['arm'])
    
    print(arm_state.get_motor_angle(request.json['arm']))
    return {"currentAngle": arm_state.get_motor_angle(request.json['arm'])}

@app.route('/changeSlider', methods=['POST', 'OPTIONS'])
def change_slider():
    if request.method == 'OPTIONS':
        return cors_preflight_response()
    
    app.logger.debug(f'Received request to change slider with value \'{request.json["move"]}\'')
    
    # If debug mode is not on, instruct the robotic arm to move
    if not app.config.get('debug'):
        arm.move(request.json['move'])
    else:
        arm_state.set_motor_angle(request.json['move'])
    
    return ""
