# Referenced from https://www.geeksforgeeks.org/python-program-that-sends-and-recieves-message-from-client/

import socket
import sys
import os
import time


# Initialize s to socket
s = socket.socket()
 
# Initialize the host
host = socket.gethostname()
 
# Initialize the port
port = 8080

# Bind the socket with port and host
s.bind(('', port))
 
print("waiting for connections...")
 
# listening for connections
s.listen()
 
# accepting the incoming connections
conn, addr = s.accept()
 
print(addr, "is connected to server")
 
# take command as input
command = input(str("Enter Command :"))
 
conn.send(command.encode())
 
print("Command has been sent successfully.")
 
# receive the confirmation
data = conn.recv(1024)
 
if data:
    print("command received and executed successfully.")