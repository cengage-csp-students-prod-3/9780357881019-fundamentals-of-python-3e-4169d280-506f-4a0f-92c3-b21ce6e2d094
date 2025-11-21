"""
File: timeserver.py
Programming Exercise 12.2 (Modified)

Server for providing the day and time. Allows the server user
to press ENTER to shut the server down. Runs on its own thread.
"""

from socket import *
from timeclienthandler import TimeClientHandler
from threading import Thread

HOST = "localhost"
PORT = 6000
ADDRESS = (HOST, PORT)


class TimeServer(Thread):
    """Day/Time server that runs until shutdown signal is given."""

    def __init__(self):
        Thread.__init__(self)
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind(ADDRESS)
        self.server.listen(5)
        self.running = True

    def run(self):
        """Main server loop, accepting clients until shutdown."""
        print("Waiting for connection . . .")

        # Keep running until quit() shuts down the socket
        while self.running:
            try:
                self.server.settimeout(1)  # prevents blocking forever
                client, address = self.server.accept()
            except timeout:
                continue
            except OSError:
                break  # Occurs after shutdown

            print("... connected from: ", address)
            handler = TimeClientHandler(client)
            handler.start()

        try:
            self.server.close()
        except:
            pass

    def quit(self):
        """Shutdown server loop and close socket."""
        self.running = False
        try:
            self.server.close()
        except:
            pass


def main():
    """Starts the server thread and waits for user input to shut down."""
    server = TimeServer()
    server.start()
    print("Press enter to shut the server down.")

    input()  # waits for shutdown command
    server.quit()
    print("Server shutting down.")


if __name__ == "__main__":
    main()
