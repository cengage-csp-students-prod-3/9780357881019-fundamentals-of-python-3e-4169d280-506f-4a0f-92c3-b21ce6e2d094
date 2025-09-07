"""
File: pcsharedcell.py
Programming Exercise 12.9

Resource for shared data synchonization for the producer-consumer
problem. Guarantees that a writer finishes writing before a reader
and conversely. Only the writer can access the data at startup.
"""

from threading import Condition
from sharedcell import SharedCell

class PCSharedCell(SharedCell):
    """Shared data that sequences reading before writing."""
    
    def __init__(self, data):
        """Can produce but not consume at startup."""
        SharedCell.__init__(self, data)
        self.writeable = True
        self.condition = Condition()
