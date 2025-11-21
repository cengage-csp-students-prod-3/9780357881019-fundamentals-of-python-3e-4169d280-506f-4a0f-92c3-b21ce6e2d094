# File: sharedcell.py

class SharedCell:
    """Base class storing shared data and providing generic read/write methods."""

    def __init__(self):
        # Initialize data with a placeholder
        self._data = None

    def write(self, data):
        """Public write method — subclasses control synchronization."""
        self.beginWrite()
        self._data = data
        self.endWrite()

    def read(self):
        """Public read method — subclasses control synchronization."""
        self.beginRead()
        result = self._data
        self.endRead()
        return result

    # These methods will be overridden by subclasses
    def beginRead(self): pass
    def endRead(self): pass
    def beginWrite(self): pass
    def endWrite(self): pass
