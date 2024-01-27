from flask import Flask, request

app = Flask(__name__)

@app.get('/liveness')
def liveness_probe():
    app.logger.info(f'Received liveness probe, responding...')
    return {'uuid': app.config.get('uuid')}
