# Write your code here
# File: phonebookclient.py

from socket import *
from codecs import decode

HOST = "127.0.0.1"
PORT = 5000

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print(decode(s.recv(1024), "utf-8"))

while True:
    message = input("> ")
    s.send(bytes(message + "\n", "utf-8"))

    if message.upper() == "QUIT":
        print(decode(s.recv(1024), "utf-8"))
        break

    reply = decode(s.recv(1024), "utf-8")
    print(reply)

s.close()
