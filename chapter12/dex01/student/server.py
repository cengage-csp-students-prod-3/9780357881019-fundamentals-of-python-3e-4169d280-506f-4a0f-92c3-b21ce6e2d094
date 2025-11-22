"""
File: server.py
"""
from socket import *
from codecs import decode

HOST = "localhost"
PORT = 5000         # Changed to match client
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(1)

print("Server ready and waiting for a connection...")
client, addr = server.accept()
print("Connected to:", addr)
