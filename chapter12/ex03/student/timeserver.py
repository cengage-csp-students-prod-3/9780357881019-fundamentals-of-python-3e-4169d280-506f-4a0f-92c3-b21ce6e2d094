"""
File: timeserver.py
Programming Exercise 12.2 Modified

Allows server-side shutdown by pressing Enter.
"""

from socket import *
from threading import Thread
from time import ctime

HOST = ''
PORT = 50007
BUFSIZE = 1024
ADDR = (HOST, PORT)


class TimeServer(Thread):
    """Day/Time Server allowing manual shutdown."""

    def __init__(self):
        Thread.__init__(self)
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind(ADDR)
        self.server.listen(5)
        self.running = True

    def run(self):
        """Wait continuously for client connections until shutdown."""
        print("Waiting for connection . . .")

        while self.running:
            try:
                self.server.settimeout(1)  # Allows periodic checking if shutting down
                client, address = self.server.accept()
            except timeout:
                continue  # Check shutdown flag again
            except OSError:
                break  # socket closed externally, shutdown complete

            print("... connected from:", address)
            client.send(bytes(ctime() + "\nHave a nice day!", "utf-8"))
            client.close()

        try:
            self.server.close()
        except:
            pass

    def quit(self):
        """Stops server loop."""
        self.running = False
        try:
            self.server.close()
        except:
            pass


def main():
    """Main thread allowing server shutdown from keyboard."""
    server = TimeServer()
    server.start()
    print("Press enter to shut the server down.")

    # User presses Enter → shutdown
    input()
    server.quit()
    print("Server shutting down.")


if __name__ == "__main__":
    main()
