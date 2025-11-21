"""
File: sharedcell.py
Parent class containing shared behavior for transcript handling.
"""

import threading

class SharedCell(object):
    """A shared cell that supports synchronized read and write operations."""

    def __init__(self, data=None):
        self._data = data
        self._lock = threading.Lock()
        self._read_ready = threading.Condition(self._lock)
        self._write_ready = threading.Condition(self._lock)
        self._readers = 0

        # Transcript storage — moved from Transcript/SharedTranscript
        self._items = [] if data is None else [data]

    # Readers/Writers protocol methods --------------------

    def read(self):
        with self._read_ready:
            self._readers += 1
        data = self._data
        with self._read_ready:
            self._readers -= 1
            if self._readers == 0:
                self._write_ready.notify()
        return data

    def write(self, data):
        with self._write_ready:
            while self._readers > 0:
                self._write_ready.wait()
            self._data = data

    # Shared transcript behavior ---------------------

    def add(self, item):
        """Adds a new entry to the transcript."""
        self._items.append(item)

    def __str__(self):
        """Returns the transcript as a newline-separated string."""
        return "\n".join(self._items)
