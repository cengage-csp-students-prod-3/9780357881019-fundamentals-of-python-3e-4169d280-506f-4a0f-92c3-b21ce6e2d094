"""
File: timeclient.py
Programming Exercise 12.2

Client for obtaining the day and time. Recovers from connection
errors.
"""

from socket import *
from codecs import decode

HOST = "localhost" 
PORT = 6000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

try:
    server = socket(AF_INET, SOCK_STREAM)               # Create a socket
    server.connect(ADDRESS)                             # Connect it to a host
    dayAndTime = decode(server.recv(BUFSIZE), "ascii")  # Read a string from it
    print(dayAndTime)
    server.close()                                      # Close the connection
except ConnectionRefusedError:
    print("Error connecting to the server.")
