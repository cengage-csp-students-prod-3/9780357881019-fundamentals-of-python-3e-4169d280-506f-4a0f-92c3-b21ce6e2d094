"""
ATM Application Server
"""

from socket import socket, AF_INET, SOCK_STREAM
from atm import Bank, ATM
from atmclienthandler import ATMClientHandler

HOST = "localhost"
PORT = 5000

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("ATM server started. Waiting for clients...")

bank = Bank()
atm = ATM(bank)

while True:
    client, addr = server.accept()
    print("Client connected:", addr)
    handler = ATMClientHandler(client, atm)
    handler.start()
