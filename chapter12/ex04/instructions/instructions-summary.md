<!-- manual -->

## Instructions

Modify the doctor application discussed in this chapter so that it tracks clients by name and history. A `Doctor` object has its own history list of a patient’s inputs for generating replies that refer to earlier conversations, as discussed in Chapter 5.

A `Doctor` object (in the file **doctor.py**) is now associated with a patient’s name. The client application (in the file **doctorclient.py**) takes this name as input and sends it to the client handler (in the file **doctorclienthandler.py**) when the patient connects.

Update the **doctorclienthandller.py** file so the`DoctorClientHandler` class checks for a pickled file with the patient’s name as its filename ("**[patient name].dat**”). If that file exists, it will contain the patient’s history, and the client handler loads the file to create the `Doctor` object.

Otherwise, the patient is visiting the doctor for the first time, so the client handler creates a brand-new `Doctor` object. When the client disconnects, the client handler pickles the `Doctor` object in a file with the patient’s name. (LO: 12.1, 12.3)

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 doctorserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 doctorclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

An example of the program is shown below:

<img src="../assets/chapter12ex04-1.png" alt='A classic Windows-OS-style dialog box titled "Doctor" with a light blue background. At the top, a prompt reads, "Please enter your name to connect." Below the prompt is a white rectangular text input field for the user to type their name. Under the input box, there are two buttons: the left button labeled "Send reply" is grayed out and disabled, while the right button labeled "Connect" is enabled and clickable. The window has a standard Windows OS control bar with minimize, maximize, and close buttons in the top right corner.'>

## Your Tasks
