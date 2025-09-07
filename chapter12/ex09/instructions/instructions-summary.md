<!-- manual -->

## Instructions

Jack has been working on the shared cell classes for the producer-consumer problem and the readers and writers problem, and he notices some serious redundancy in the code. The `read` and `write` methods are the same in both classes, and both classes include an instance variable for the data.

Jill, his team manager, advises him to place this redundant code in a parent class named `SharedCell` (in the file **sharedcell.py**). Then two subclasses, named `PCSharedCell` (in the file **pcsharedcell.py**) and `RWSharedCell` (in the file **rwsharedcell.py**), can inherit this code and define the methods `beginRead`, `endRead`, `beginWrite`, and `endWrite`, to enforce their specific synchronization protocols.

Also, the `__init__` method in each subclass first calls the `__init__` method in the `SharedCell` class
to set up the data, and then adds the condition(s) and other instance variables for its specific situation. Jack has called in sick, so you must complete this hierarchy of classes and redo the demo programs (in the files **producerconsumer.py** and **readersandwriters.py**) so that they use them. (LO: 12.1, 12.2)

An example of the program is shown below:

```
Enter the number of accesses: 3
Starting the threads
Producer starting up
Consumer starting up

Counter value is 1
Counter value is 2
Producer is done producing

Counter value is 3
Consumer is done consuming
```

## Your Tasks
