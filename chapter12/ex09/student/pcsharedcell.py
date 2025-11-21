# File: pcsharedcell.py

from threading import Condition
from sharedcell import SharedCell

class PCSharedCell(SharedCell):
    """Shared cell enforcing Producer/Consumer synchronization rules."""

    def __init__(self):
        super().__init__()
        self._condition = Condition()
        self._full = False   # Tracks whether the cell contains unread data

    def beginRead(self):
        with self._condition:
            while not self._full:
                self._condition.wait()

    def endRead(self):
        with self._condition:
            self._full = False
            self._condition.notify_all()

    def beginWrite(self):
        with self._condition:
            while self._full:
                self._condition.wait()

    def endWrite(self):
        with self._condition:
            self._full = True
            self._condition.notify_all()
