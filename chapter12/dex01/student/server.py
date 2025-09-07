"""
File: server.py
"""
from socket import *
from codecs import decode
HOST = "localhost"
PORT = 6000
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
"""
File: client.py
"""
from socket import *
from codecs import decode
HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
server = socket(AF_INET, SOCK_STREAM) # Create a socket
server.connect(ADDRESS) # Connect it to a host