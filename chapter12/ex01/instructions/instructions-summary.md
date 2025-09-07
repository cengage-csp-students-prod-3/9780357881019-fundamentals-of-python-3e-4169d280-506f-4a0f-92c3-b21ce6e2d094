<!-- manual -->

## Instructions

Redo the producer/consumer program (in the file **pc.py**) so that it allows multiple consumers. Each consumer must be able to consume the same data before the producer produces more data. (LO: 12.1)

An example of the program is shown below:

```
Enter the number of consumers: 3
Enter the number of accesses: 2
Starting the threads
Producer starting up

Consumer 0 starting up

Consumer 1 starting up

Consumer 2 starting up

Producer setting data to 1
Consumer 1 accessing data 1
Consumer 2 accessing data 1
Consumer 0 accessing data 1
Producer setting data to 2
Producer is done producing

Consumer 1 accessing data 2
Consumer 1 is done consuming

Consumer 2 accessing data 2
Consumer 2 is done consuming

Consumer 0 accessing data 2
Consumer 0 is done consuming

```

## Your Tasks
