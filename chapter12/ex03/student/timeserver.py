"""
File: timeserver.py
Modified Programming Exercise 12.2

Time server that allows shutting down by pressing ENTER.
"""

from socket import *
from threading import Thread
from time import ctime
from timeclienthandler import TimeClientHandler


class TimeServer(Thread):

    def __init__(self, port=50000):
        Thread.__init__(self)
        self.host = ""
        self.port = port
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(5)

        self.running = True  # server control flag

    def run(self):
        print("Waiting for connection . . .")
        while self.running:
            self.serverSocket.settimeout(1)  # prevents blocking during shutdown check
            try:
                client, address = self.serverSocket.accept()
                print("... connected from:", address)
                handler = TimeClientHandler(client)
                handler.start()
            except timeout:
                continue  # loop again to check if shutting down

        self.serverSocket.close()
        print("Server shut down.")

    def quit(self):
        """Signals the server loop to stop."""
        self.running = False

    @staticmethod
    def main():
        server = TimeServer()
        server.start()  # start server thread

        input("Press enter to shut the server down.\n")
        server.quit()

        print("Server shutting down.")
        server.join()


if __name__ == "__main__":
    TimeServer.main()
