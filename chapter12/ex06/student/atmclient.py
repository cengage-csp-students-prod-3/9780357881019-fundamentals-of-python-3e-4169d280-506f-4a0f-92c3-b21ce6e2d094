"""
ATM Client program
"""

from socket import socket, AF_INET, SOCK_STREAM

HOST = "localhost"
PORT = 5000

class ATMClient:

    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((HOST, PORT))
        print(self.client.recv(1024).decode())

    def send(self, message):
        self.client.send(message.encode())
        return self.client.recv(1024).decode()

    def close(self):
        self.client.send(b"QUIT")
        self.client.close()


def main():
    atm = ATMClient()

    acct = input("Enter account number: ")
    pin = input("Enter PIN: ")
    print(atm.send(f"LOGIN {acct} {pin}"))

    while True:
        print("\n1) Deposit\n2) Withdraw\n3) Balance\n4) Quit")
        choice = input("> ")

        if choice == "1":
            amt = input("Amount: ")
            print(atm.send(f"DEPOSIT {amt}"))
        elif choice == "2":
            amt = input("Amount: ")
            print(atm.send(f"WITHDRAW {amt}"))
        elif choice == "3":
            print(atm.send("BALANCE"))
        elif choice == "4":
            atm.close()
            break

if __name__ == "__main__":
    main()
