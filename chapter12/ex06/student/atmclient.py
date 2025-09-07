"""
File: atmclient.py
Project 10.6
This module defines the ATMClient class, which provides a window
for bank customers to perform deposits, withdrawals, and check
balances remotely via a client.
"""

from socket import *
from codecs import decode
from breezypythongui import EasyFrame

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = "ascii"

class ATMClient(EasyFrame):
    """Represents an ATM window for a client. The window connects to the server at startup and waits for customers to login, then sends requests to the server. Does not disconnect from server at logout, but waits for new login request from user.
    """

    def __init__(self):
        """Initialize the frame and connect to the server."""
        EasyFrame.__init__(self, title = "ATM")
        """Create and add the widgets to the window."""
        # TODO: Create the user interface using the UI elements below.
        # self.nameLabel()
        # self.pinLabel()
        # self.amountLabel()
        # self.statusLabel()
        # self.nameField()
        # self.pinField()
        # self.amountField()
        # self.statusField()
        # self.balanceButton
        # self.depositButton()

        """Connect to server and confirm connection"""
        # Add your code here            

    def login(self):
        """Attempts to login the customer.  If successful,
        enables the buttons, including logout."""
        # Add your code here
        # TODO: Retrieve the user's login information
        # TODO: Send the user's login credentials to the server with the LOGIN code
        # TODO: Receive the server's response and handle appropriately
        # Reply will be the empty string if login succeeds
        
    def logout(self):
        """Logs the customer out, clears the fields, disables the buttons, and enables login."""
        # Add your code here
        # TODO: Send the server the LOGOUT code
        # TODO: Reset the interface so the user is denied access until they login again


    def getBalance(self):
        """Displays the current balance in the status field."""
        # Add your code here
        # TODO: Send the server the BALANCE code
        # TODO: Handle the server's response appropriately and update the statusField with the balance 

    def deposit(self):
        """Attempts a deposit. If not successful, displays
        error message in statusfield; otherwise, announces
        success."""
        # Add your code here
        # TODO: Retrieve the amount the user wants to deposit into their account
        # TODO: Send the deposit amount to the server using the DEPOSIT code
        # TODO: Handle the server's response appropriately and update the statusField 

        
    def withdraw(self):
        """Attempts a withdrawal. If not successful, displays error message in statusfield; otherwise, announces success."""
        # Add your code here
        # TODO: Retrieve the amount the user wants to withdraw. 
        # TODO: Send the withdrawal amount to the server with the WITHDRAW code
        # TODO: Handle the server's response appropriately and update the statusField 
        
def main(fileName = None):
    """Creates the bank with the optional file name,
    wraps the window around it, and opens the window.
    Saves the bank when the window closes."""
    ATMClient().mainloop()

if __name__ == "__main__":
    main()