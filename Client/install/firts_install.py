import os
import sys
sys.path.append("Client")
from modules.info_server import *

def main():
    # Get the path of the client
    path = os.getcwd()
    # Get the name of the client
    name = os.path.basename(path)
    # Get the ip of the server
    ip = get_ip()
    # Get the port of the server
    port = get_port()
    # Get the name of the server
    server_name = get_server_name()
    # Get the name of the server
    server_name = get_server_name()
    # Create the file
    file = open("Client\config\config.ini", "w")
    # Write the data
    file.write("[SERVER]
