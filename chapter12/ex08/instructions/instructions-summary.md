<!-- manual -->

## Instructions

Add synchronization to the ATM program of _Programming Exercise 6_. You will need to give concurrent readers access to a single account, as long as a writer is not writing to it, and give a single writer access, as long as other writers and readers are not accessing the account.

Hint: Complete the `ThreadSafeSavingsAccount` class (in the file **threadsafesavingsaccount.py**) discussed in this chapter, and use it to create account objects in the `Bank` class (**bank.py**).

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 atmserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 atmclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

<!--
{
    "CopyExercise": {
        "name": "Chapter 12, Exercise 06",
        "copyTarget": "/chapter12/ex06/student/*",
        "pasteTarget": "/"
    }
}
-->

An example of the program is shown below:

<img src="../assets/chapter12ex08-1.png" alt='Retro-styled window titled "ATM" with a blue title bar and minimize, maximize, and close buttons. The interface contains four labeled fields: "Name" with an empty input box, "Pin" with an empty input box, "Amount" with the value 0.0, and "Status" displaying "Welcome to the bank!". To the right are four buttons: "Balance", "Deposit", and "Withdraw" are disabled; "Login" is enabled. The design resembles a classic Windows OS application.
'>

## Your Tasks
