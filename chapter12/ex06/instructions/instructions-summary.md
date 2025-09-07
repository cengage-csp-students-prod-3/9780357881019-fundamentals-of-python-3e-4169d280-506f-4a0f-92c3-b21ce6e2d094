<!-- manual -->

## Instructions

Convert the ATM application presented in _Chapter 9, Exercise 4_ (**atm.py**) to a networked application.

A brief overview of each file is given below. Make sure you read the docstring and the comments within each file as they contain `TODO:` to assist in the implementation.

The client (in the file **atmclient.py**) manages the user interface and creates the socket connections with the application's server (in the file **atmserver.py**). The `ATMClient` class forwards the user's information to the server and manages the server response by updating the GUI.

The server (**atmserver.py**) and client handler (in the file **atmclienthandler.py**) manage connecting to the `ATM` class and transactions with the `Bank` class. When the server is run, it begins to listen for a connection to be established. The server is responsible for starting and hosting the `ATMClientHandler` thread.

The `ATMClientHandler` interprets the information received from the `ATMClient` class, and interfaces with the `ATM` and `Bank` classes in order to respond appropriately.

Design, implement, and test a network application that maintains clients of a bank when making transactions at an atm. The data model for the accounts are saved in a file that holds all the savings accounts.

Clients should be able to deposit and withdraw money from their account and view their balance from the atm. The server should handle multiple clients without delays.

> Be sure to use the field names provided in the comments in your starter code.

Do not be concerned about synchronization problems in this project.

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 atmserver.py` into the first **Terminal** or click **Run** with the file open.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 atmclient.py` into the second **Terminal** or click **Run** with the file open.

> The client code will now be able to establish a connection to the server.

<!--
{
    "CopyExercise": {
        "name": "Chapter 9, Exercise 04",
        "copyTarget": "/chapter9/ex04/student/",
        "pasteTarget": "/"
    }
}
-->

An example of the program is shown below:
<img src="../assets/chapter12ex06-1.png" alt='Retro-styled window titled "ATM" with a blue title bar and minimize, maximize, and close buttons. The interface contains four labeled fields: "Name" with an empty input box, "Pin" with an empty input box, "Amount" with the value 0.0, and "Status" displaying "Welcome to the bank!". To the right are four buttons: "Balance", "Deposit", and "Withdraw" are disabled; "Login" is enabled. The design resembles a classic Windows OS application.
'>

## Your Tasks
