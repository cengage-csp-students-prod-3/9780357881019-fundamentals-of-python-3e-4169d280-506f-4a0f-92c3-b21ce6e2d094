"""
File: producerconsumer3.py
Programming Exercise 12.9

Producer-consumer demo with synchronization.
Producer and consumer both access shared data a given number
of times. They sleep a random interval before each access.
The data must be produced before it is consumed, and be produced
and consumed just once.
The condition and Boolean flag on the shared data guarantee that
the producer and consumer access the data in the correct order.
"""

import time, random
from threading import Thread
from pcsharedcell import PCSharedCell
from counter import Counter

class Producer(Thread):
    """A producer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepInterval):
        Thread.__init__(self, name = "Producer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepInterval = sleepInterval

    def run(self):
        """Resets the data in the cell and goes to sleep,
        the given number of times."""
        print("%s starting up" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepInterval))
            self.cell.write(lambda counter: counter.increment())
        print("%s is done producing\n" % self.getName())

class Consumer(Thread):
    """A consumer of data in a shared cell."""

    def __init__(self, cell, accessCount, sleepInterval):
        Thread.__init__(self, name = "Consumer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepInterval = sleepInterval

    def run(self):
        """Accesses the data in the cell and goes to sleep,
        the given number of times."""
        print("%s starting up\n" % self.getName())
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepInterval))
            value = self.cell.read(lambda counter: counter.getValue())
            print("Counter value is", value)
        print("%s is done consuming\n" % self.getName())

def main():
    accessCount = int(input("Enter the number of accesses: "))
    counter = Counter()
    cell = PCSharedCell(counter)
    p = Producer(cell, accessCount, 4)
    c = Consumer(cell, accessCount, 4)
    print("Starting the threads")
    p.start()
    c.start()

if __name__ == "__main__":
    main()

