<!-- manual -->

## Instructions

A crude multi-client chat room allows two or more users to converse by sending and receiving messages. On the client side (in the file **chatclient.py**), a user connects to the chat room as in the ATM application, by clicking a **Connect** button.

At that point, a transcript of the conversation thus far appears in a text area. At any time, the user can send a message to the chat room by entering it as input and clicking a **Send** button.

When the user sends a message, the chat room returns another transcript of the entire conversation to display in the text area. The user disconnects by clicking the **Disconnect** button.

On the server side, there are five resources: a server, a client handler, a transcript, a thread-safe transcript, and a shared cell. Their roles are much the same as they are in the ATM application of Programming Exercise 8.

The server (in the file **chatserver.py**) creates a thread-safe transcript at start-up, listens for client connections, and passes a client’s socket and the thread-safe transcript (in the file **threadsafetranscript.py**) to a client handler when a client connects (in the file **chatclienthandler.py**). The client handler receives the client’s name from the client socket, adds this name and the connection time to the thread-safe transcript, sends the thread-safe transcript’s string to the client, and waits for a reply.

When the client’s reply comes in, the client handler adds the client’s name and time to it, adds the result to the thread-safe transcript, and sends the thread-safe transcript’s string back to the client. When the client disconnects, their name and a message to that effect are added to the thread-safe transcript.

The `SharedCell` class includes the usual `read` and `write` methods for a readers and writers protocol, and the `SharedTranscript` and `Transcript` classes include an `add` method and an `__str__` method. The `add` method adds a string to a list of strings, while `__str__` returns the `join` of this list, separated by newlines. (LO: 12.1, 12.2, 12.3)

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 chatserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 chatclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

An example of the program is shown below:

<img src="../assets/chapter12ex10-1.png" alt='Retro-style window titled "Chat Room" with a blue title bar and classic minimize, maximize, and close buttons in the top-right corner. The interface is divided into three sections. At the top is the label "Transcript of the chat:" followed by a large, empty, scrollable text area intended to display the chat log. Below is the label "Want to connect?" followed by a second empty, scrollable text area, likely for user input. At the bottom are two buttons: "Send" on the left, which is grayed out and disabled, and "Connect" on the right, which is active and clickable. The layout mimics an old Windows OS application.'>

## Your Tasks
