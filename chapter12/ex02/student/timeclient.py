from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)

try:
    tcpCliSock.connect(ADDR)
except ConnectionRefusedError:
    print("Error connecting to the server")
    exit()

data = tcpCliSock.recv(BUFSIZE)
print(data.decode())
print("Have a nice day!")

tcpCliSock.close()
