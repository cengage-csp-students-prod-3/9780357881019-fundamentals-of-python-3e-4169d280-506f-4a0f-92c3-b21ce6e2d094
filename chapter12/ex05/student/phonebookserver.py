# Write your code here
# File: phonebookserver.py

from socket import *
from phonebook import PhoneBook
from phonebookclienthandler import PhoneBookClientHandler

HOST = ""
PORT = 5000

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print("Phone Book Server running...")

# Create shared phonebook object (ONE for all clients)
phonebook = PhoneBook()

while True:
    client, addr = s.accept()
    print(f"Connected to {addr}")
    handler = PhoneBookClientHandler(client, phonebook)
    handler.start()
