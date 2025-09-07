"""
File: timeclienthandler.py
Programming Exercise 12.2

Client handler for providing the day and time.
"""

from time import ctime
from threading import Thread
from codecs import decode

class TimeClientHandler(Thread):
    """Handles a client request."""
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
   
    def run(self):
        self.client.send(bytes(ctime() + \
                               "\nHave a nice day!",
                               "ascii"))
        self.client.close()


