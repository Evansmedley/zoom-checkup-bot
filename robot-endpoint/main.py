import argparse
from HTTPClient import HTTPClient
from flask_app import app


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
    uuid = HTTPClient(args.name).register(args.server, args.listen_port, args.local)
    
    app.config['name'], app.config['uuid'], app.config['debug'] = \
                    args.name, uuid, args.debug
    
    if args.debug:
        print(f'Starting Flask app listening on {"127.0.0.1"}:{args.listen_port}...')
        app.run(host='127.0.0.1', port=args.listen_port)
    else:
        app.run(host='127.0.0.1', port=args.listen_port)
