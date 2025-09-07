"""
File: atmclienthandler.py
Project 10.6
Client handler for ATM. Receives Bank object from
the server, and accesses acccounts via login requests.

Request syntax:

LOGIN name pin
LOGOUT
BALANCE
DEPOSIT amount
WITHDRAW amount

"""

from socket import *
from codecs import decode
from threading import Thread

BUFSIZE = 1024
CODE = "ascii"

class ATMClientHandler(Thread):
    """Handles ATM requests from a client."""
    
    def __init__(self, client, bank):
        """Save references to the client socket and bank."""
        # Add your code here
        Thread.__init__(self)
        # TODO: Create a reference to the client object
        # TODO: Create a reference to the bank object

    def interpret(self, request):
        """Interprets a request and returns a message."""
        """This method does not communicate with the server / client."""
        # Add your code here
        # TODO: Handle the CODE ("request") for LOGIN
        # TODO: Handle the CODE ("request") for LOGOUT
        # TODO: Handle the CODE ("request") for BALANCE
        # TODO: Handle the CODE ("request") for DEPOSIT
        # TODO: Handle the CODE ("request") for WITHDRAW
   
    def run(self):
        """Sends a greeting to the client, then enters
        an interative loop to take and respond to
        requests."""
        # Add your code here
        # TODO: Send an initial greeting message to the client 
        # TODO: Create a loop to run until the client disconnects
        # TODO: Receive the request from the client
        # TODO: Interpret the client's request
        # TODO: Send the response back to the client