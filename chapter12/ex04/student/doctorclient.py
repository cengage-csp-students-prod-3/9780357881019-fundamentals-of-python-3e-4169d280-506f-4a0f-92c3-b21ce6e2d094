"""
File: doctorclient.py
"""

from socket import socket

HOST = 'localhost'
PORT = 5000

def main():
    s = socket()
    s.connect((HOST, PORT))

    # Get user name
    name = input("Enter your name: ")
    s.send(name.encode("ascii"))

    # Receive greeting
    print(s.recv(1024).decode("ascii"))

    # Chat loop
    while True:
        message = input("> ")

        if message.lower() == "quit":
            s.send(message.encode("ascii"))
            break

        s.send(message.encode("ascii"))
        print("\nDoctor:", s.recv(1024).decode("ascii"))

    s.close()

if __name__ == "__main__":
    main()
