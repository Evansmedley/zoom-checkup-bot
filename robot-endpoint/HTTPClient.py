import requests
import uuid
import socket
import json
import sys

SERVER_PORT = 8080
ENDPOINT_PATH = "/endpoint/register"
MAX_ATTEMPTS = 5

class HTTPClient():
    
    def __init__(self, name: str):
        self.name = name
        
    def do_post(self, dest_addr: str, payload: dict, headers: dict):
        attempt_counter = 0
        while attempt_counter < MAX_ATTEMPTS:
            try:
                attempt_counter += 1
                response = requests.post(dest_addr, data=json.dumps(payload), headers=headers)
                break
            except requests.ConnectTimeout as error:
                print(error)
                if attempt_counter >= MAX_ATTEMPTS:
                    sys.exit(1)
            except requests.ConnectionError as error:
                print(error)
                sys.exit(1)
        
        return response
    
    
    def get_external_client_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    
                
    def register(self, server_host: str, listen_port: int, local=False):
        dest_addr = f"http://{server_host}:{SERVER_PORT}{ENDPOINT_PATH}"
        print(f"URI of server to register with -> {dest_addr}")
    
        client_ip = '127.0.0.1' if local else self.get_external_client_ip()
        
        print(f"CLIENT IP -> {client_ip}")
    
        payload = {
            'uuid': str(uuid.uuid4()),
            'name': self.name,
            'ip': client_ip,
            'port': listen_port,
            'active': False
        }
    
        headers = {
            'Content-Type': 'application/json'
        }
        
        return self.do_post(dest_addr, payload, headers).json()['uuid']
