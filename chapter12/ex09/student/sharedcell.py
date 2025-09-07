"""
File: sharedcell.py
Programming Exercise 12.9

Abstract resource for shared data synchonization for readers and writers
problems. Includes the read and write methods and the shared data.
Subclasses will add conditions, counts, and flags, as well as
beginRead, endRead, beginWrite, and endWrite.
"""

from threading import Condition

class SharedCell(object):
    """Synchronizes readers and writers around shared data,
    with specific protocols determined by subclasses."""
    
    def __init__(self, data):
        """Sets up the data."""
        self.data = data
        

