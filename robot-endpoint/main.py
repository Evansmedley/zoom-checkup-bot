import argparse
from HTTPClient import HTTPClient
from flask_app import app
import subprocess


def get_args():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-n', '--name', action='store', type=str, 
                        help='Desired name of endpoint', required=True)
    parser.add_argument('-s', '--server', action='store', type=str, 
                        help='Address for contacting the server', required=True)
    parser.add_argument('-p', '--listen_port', action='store', type=int, 
                        help='Port to listen on', default=8080, required=False)
    parser.add_argument('-d', '--debug', action='store_true', 
                        help='Debug mode -> print events rather than actually controlling the robotic arm')
    parser.add_argument('-l', '--local', action='store_true', 
                        help='Local mode -> for running endpoint on same network as server, uses internal ip instead of external ip')
    
    args = parser.parse_args()
    
    return args


if __name__ == '__main__':
    
    args = get_args()
    
    # Send a POST request to the server to register
    http_client = HTTPClient(args.name)
    uuid = http_client.register(args.server, args.listen_port, args.local)

    # Start camera streaming
    camera_process = subprocess.Popen(['python3', 'camera.py'])
    
    app.config['name'], app.config['uuid'], app.config['debug'] = \
                    args.name, uuid, args.debug
    
    server_ip = '127.0.0.1' if args.local else http_client.get_external_client_ip()
    
    print(f'Starting Flask app listening on {server_ip}:{args.listen_port}...')

    app.run(host=server_ip, port=args.listen_port)
