from flask import Flask, request

app = Flask(__name__)

@app.post('/liveness')
def liveness_probe():
    app.logger.info(f'Received liveness probe, responding...')
    if app.config.get('uuid') != request.json['uuid']:
        return {"message": "Bad Request, invalid uuid"}, 400
    else:
        return {'uuid': app.config.get('uuid')}
