# File: rwsharedcell.py

from threading import Condition
from sharedcell import SharedCell

class RWSharedCell(SharedCell):
    """Shared cell enforcing Readers/Writers synchronization."""

    def __init__(self):
        super().__init__()
        self._condition = Condition()
        self._readers = 0
        self._writerActive = False

    def beginRead(self):
        with self._condition:
            while self._writerActive:
                self._condition.wait()
            self._readers += 1

    def endRead(self):
        with self._condition:
            self._readers -= 1
            if self._readers == 0:
                self._condition.notify_all()

    def beginWrite(self):
        with self._condition:
            while self._writerActive or self._readers > 0:
                self._condition.wait()
            self._writerActive = True

    def endWrite(self):
        with self._condition:
            self._writerActive = False
            self._condition.notify_all()
