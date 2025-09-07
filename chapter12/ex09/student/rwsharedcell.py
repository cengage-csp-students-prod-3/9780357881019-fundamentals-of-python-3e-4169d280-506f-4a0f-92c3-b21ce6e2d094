"""
File: rwsharedcell.py
Programming Exercise 12.9

Resource for shared data synchonization for the general readers and writers
problem. Guarantees that a writer finishes writing before readers can
read and other writers can write. Also supports concurrent reading.
"""

from threading import Condition
from sharedcell import SharedCell

class RWSharedCell(SharedCell):
    """Synchronizes readers and writers around shared data,
    to support concurrent reading and safe writing."""
    
    def __init__(self, data):
        """Sets up the conditions and count of active readers."""
        SharedCell.__init__(self, data)
        self.writing = False
        self.readerCount = 0
        self.okToRead = Condition()
        self.okToWrite = Condition()

    