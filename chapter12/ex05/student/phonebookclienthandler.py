# Write your code here
# File: phonebookclienthandler.py

from threading import Thread
from codecs import decode

class PhoneBookClientHandler(Thread):
    """Handles communication with a connected client."""

    def __init__(self, client, phonebook):
        Thread.__init__(self)
        self.client = client
        self.phonebook = phonebook

    def run(self):
        self.client.send(bytes("Welcome to the Online Phone Book!\n", "utf-8"))
        self.client.send(bytes("Commands:\nLOOKUP name\nADD name number\nQUIT\n", "utf-8"))

        while True:
            request = decode(self.client.recv(1024), "utf-8")

            if not request:
                break

            parts = request.strip().split()

            if len(parts) == 0:
                continue

            command = parts[1] if parts[0].strip() == "" else parts[0].upper()

            if command == "LOOKUP" and len(parts) >= 2:
                name = " ".join(parts[1:])
                result = self.phonebook.lookup(name)
                if result:
                    self.client.send(bytes(f"{name}'s number is {result}\n", "utf-8"))
                else:
                    self.client.send(bytes(f"{name} not found.\n", "utf-8"))

            elif command == "ADD" and len(parts) >= 3:
                name = parts[1]
                number = parts[2]
                self.phonebook.add(name, number)
                self.client.send(bytes(f"Added {name} with number {number}.\n", "utf-8"))

            elif command == "QUIT":
                self.client.send(bytes("Goodbye!\n", "utf-8"))
                break

            else:
                self.client.send(bytes("Invalid command.\n", "utf-8"))

        self.client.close()
