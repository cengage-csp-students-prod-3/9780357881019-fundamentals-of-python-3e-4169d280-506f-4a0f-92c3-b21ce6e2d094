"""
Handles a single ATM client.
"""

from threading import Thread
from codecs import decode, encode

class ATMClientHandler(Thread):

    def __init__(self, client, atm):
        Thread.__init__(self)
        self.client = client
        self.atm = atm

    def run(self):
        self.client.send(b"CONNECTED\n")
        while True:
            message = decode(self.client.recv(1024), "ascii").strip()
            if not message or message == "QUIT":
                self.client.close()
                break

            parts = message.split()
            cmd = parts[0].upper()

            if cmd == "LOGIN":
                _, acct, pin = parts
                result = self.atm.authenticate(acct, pin)
                self.client.send(encode(f"LOGIN {'SUCCESS' if result else 'FAIL'}\n", "ascii"))

            elif cmd == "DEPOSIT":
                amount = float(parts[1])
                self.atm.deposit(amount)
                self.client.send(b"DEPOSIT OK\n")

            elif cmd == "WITHDRAW":
                amount = float(parts[1])
                success = self.atm.withdraw(amount)
                self.client.send(encode("WITHDRAW OK\n" if success else "WITHDRAW FAIL\n", "ascii"))

            elif cmd == "BALANCE":
                bal = self.atm.balance()
                self.client.send(encode(f"BALANCE {bal:.2f}\n", "ascii"))
