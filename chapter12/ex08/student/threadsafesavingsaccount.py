"""
Thread-safe version of the SavingsAccount class.
"""

from threading import Condition

class ThreadSafeSavingsAccount(object):

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

        # Reader-writer lock variables
        self.condition = Condition()
        self.readers = 0
        self.writer_active = False

    # ------------ Reader Entry / Exit ------------

    def _start_read(self):
        with self.condition:
            while self.writer_active:
                self.condition.wait()
            self.readers += 1

    def _end_read(self):
        with self.condition:
            self.readers -= 1
            if self.readers == 0:
                self.condition.notify_all()

    # ------------ Writer Entry / Exit ------------

    def _start_write(self):
        with self.condition:
            while self.writer_active or self.readers > 0:
                self.condition.wait()
            self.writer_active = True

    def _end_write(self):
        with self.condition:
            self.writer_active = False
            self.condition.notify_all()

    # ------------ Public Account Methods ------------

    def get_balance(self):
        """Safe read."""
        self._start_read()
        result = self.balance
        self._end_read()
        return result

    def deposit(self, amount):
        """Safe write."""
        self._start_write()
        self.balance += amount
        self._end_write()

    def withdraw(self, amount):
        """Safe write."""
        self._start_write()
        if amount > self.balance:
            self._end_write()
            return False
        self.balance -= amount
        self._end_write()
        return True

    def validate_pin(self, pin):
        return self.pin == pin
