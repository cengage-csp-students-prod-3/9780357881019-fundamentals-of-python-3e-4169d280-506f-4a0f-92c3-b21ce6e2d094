## Instructions

The Doctor program described in Chapter 5 combines the data model of a doctor and the operations for handling user interaction. Restructure this program according to the model/view pattern so that these areas of responsibility are assigned to separate sets of classes.

The program should include a `Doctor` class with an interface that allows one to obtain a greeting, a signoff message, and a reply to a patient’s string.

To implement the greeting, define a method named `greeting` for the `Doctor` class that returns the string **Hello, how can I help you today?**. To implement the signoff message, define a method named `farewell` for the `Doctor` class that returns the string **Have a nice day!**.

The `reply` function returns a randomized string response and should be added as a method for the `Doctor` class.

The rest of the program, in a separate `main` program module, handles the user’s interactions with the `Doctor` object. Develop this program with a terminal-based user interface (also in **doctor.py**). (LO: 10.1, 10.2)

An example of the program is shown below:

```
Hello, how can I help you today?
> I am sick
You seem to think that you are sick?
> Yes
And what do you think about this?
> I am not feeling good
Did I just hear you say that you are not feeling good?
> Yes
Why do you believe that Yes?
> My nose is running
I would like to hear more about that.
> I have a headache too
You seem to think that you have a headache too?
> Correct
Go on.
> It doesn't stop
Did I just hear you say that It doesn't stop?
> Correct
Go on.
> That's it
And what do you think about this?
> quit
Have a nice day!
```

## Your Tasks
