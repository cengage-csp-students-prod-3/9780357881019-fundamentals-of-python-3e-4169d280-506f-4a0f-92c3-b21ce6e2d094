<!-- manual -->

## Instructions

Modify the code in the day/time server application (in **timeserver.py**) so that the user on the server side can shut the server down. That user should be able to press the return or enter key at the terminal to do this. After the enter key is pressed, the message **Server shutting down.** should be printed to the terminal and the server should shut down.

The **timeserver.py** logic will need to be converted into the class `TimeServer`. In order to shut down the server independently, the server must be running on a separate thread.

Create the logic to run the server until the signal is given to shut the server down. The `TimeServer` class should implement the following methods:

1. `__init__`
2. `run`
3. `quit`
4. `main`

The `main` method running on the server is used to interface with the server and shut down its processes.

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 timeserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 timeclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

<!--
{
    "CopyExercise": {
        "name": "Chapter 12, Exercise 02",
        "copyTarget": "/chapter12/ex02/student/*",
        "pasteTarget": "/*"
    }
}
-->

An example of the program is shown below:

```
$ python3 timeserver.py
Press enter to shut the server down.
Waiting for connection . . .
... connected from: ('127.0.0.1', 49776)
Waiting for connection . . .



$ python3 timeclient.py
Thu Apr  3 13:21:17 2025
Have a nice day!
```

## Your Tasks
