"""
File: atmserver.py
Project 10.6
Server for providing ATM access.
Uses client handlers to handle clients' requests.
"""

from socket import *
from atmclienthandler import ATMClientHandler
from bank import createBank

HOST = "localhost"
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.bind()
server.listen()
bank = createBank(5)
# Show the account credentials for testing

"""The server now just waits for connections from clients and hands sockets off to client handlers"""
# Add your code here
# TODO: While the connection is active, start the ATMClientHandler thread