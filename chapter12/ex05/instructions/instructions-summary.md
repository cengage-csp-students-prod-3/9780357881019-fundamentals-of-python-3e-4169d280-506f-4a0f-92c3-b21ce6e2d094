<!-- manual -->

## Instructions

Design, implement, and test a network application that maintains an online phone book. The data model for the phone book (in the file **phonebook.py**) is saved in a file on the server’s computer.

Clients should be able to look up a person’s phone number or add a name and number to the phone book. The server (in the file **phonebookserver.py**) should handle multiple clients without delays.

Unlike the doctor program, there should be just one phone book that all clients share. The server creates this object at start-up and passes it to the client handlers (in the file **phonebookclienthandler.py)**. (LO: 12.1, 12.3)

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 phonebookserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 phonebookclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

An example of the program is shown below:

<img src="../assets/chapter12ex05-1.png" alt='A retro-style Windows-OS dialog box titled "Phone Book" with a light blue background. The interface displays the prompt "Want to connect?" centered near the top. Below the prompt are three horizontally aligned buttons. From left to right: the "Find" button is grayed out and disabled, the "Add" button is also grayed out and disabled, and the "Connect" button is enabled and clickable. The window frame includes the standard minimize, maximize, and close buttons in the top right corner.'>

## Your Tasks
