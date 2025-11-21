"""
File: timeclient.py
Programming Exercise 12.2

Client for obtaining the day and time.
Attempts connection and safely handles connection errors.
"""

from socket import *
from codecs import decode

HOST = "localhost"
PORT = 6000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

try:
    # Create socket and attempt server connection
    server = socket(AF_INET, SOCK_STREAM)
    server.connect(ADDRESS)

    # Receive response from server
    response = server.recv(BUFSIZE)
    message = decode(response, "ascii")
    print(message)

    # Close socket when done
    server.close()

except ConnectionRefusedError:
    print("Unable to connect to the server. Please ensure it is running.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
