"""
File: timeclienthandler.py
Programming Exercise 12.2

Client handler for providing the day and time.
"""

from time import ctime
from threading import Thread

class TimeClientHandler(Thread):
    """Handles a client request."""
    
    def __init__(self, client):
        super().__init__()
        self.client = client
   
    def run(self):
        try:
            message = ctime() + "\nHave a nice day!"
            self.client.send(message.encode("ascii"))
        except Exception as e:
            print("Error sending message to client:", e)
        finally:
            self.client.close()
