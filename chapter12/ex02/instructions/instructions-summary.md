<!-- manual -->

## Instructions

Sometimes servers are down, so clients cannot connect to them. Python raises an exception of type `ConnectionRefusedError` in a client program when a network connection is refused.

> You can generate this error by running the **timeclient.py** file.

Add exception handling code to the server logic in **stimeclient.py** to catch and recover from this kind of exception. To recover from this exception, simply print the message **Error connecting to the server** and terminate the program.

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 timeserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 timeclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

In order to test your error handling logic, run `python3 timeclient.py` into the terminal without starting the timesever. If you have already started the timeserver, use `CTL+C` to terminate the process or close the terminal window which is running the timeserver.

An example of the program is shown below:

```
$ python3 timeserver.py
Waiting for connection . . .
... connected from:  ('127.0.0.1', 34128)
Waiting for connection . . .

$ python3 timeclient.py
Thu Apr  3 13:15:09 2025
Have a nice day!
```
