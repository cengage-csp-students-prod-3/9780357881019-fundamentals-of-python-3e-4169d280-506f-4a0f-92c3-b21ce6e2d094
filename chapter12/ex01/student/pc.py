"""
File: pc.py
Programming Exercise 12.1

Illustrates the producer/consumer problem with
thread synchronization.  Makes producer wait until multiple
consumers read each datum.
"""

import time, random
from threading import Thread, current_thread, Condition

class SharedCell(object):
    """Shared data for the producer/consumer problem."""

    def __init__(self, numConsumers):
        self.numConsumers = numConsumers
        self.waitList = []
        self.data = -1
        self.writeable = True
        self.condition = Condition()
        self.consumerCondition = Condition()

    def setData(self, data):
        """Producer writes to shared data."""
        with self.condition:
            while not self.writeable:
                self.condition.wait()

            print(f"{current_thread().name} setting data to {data}")
            self.data = data
            self.writeable = False
            self.condition.notify_all()

    def getData(self):
        """Consumer reads shared data."""

        # If this consumer already read this data, wait until it's updated
        if current_thread() in self.waitList:
            with self.consumerCondition:
                self.consumerCondition.wait()

        with self.condition:
            while self.writeable:
                self.condition.wait()

            print(f"{current_thread().name} accessing data {self.data}")

            # If this is the last consumer to read the data:
            if len(self.waitList) == self.numConsumers - 1:
                self.waitList = []
                self.writeable = True
                # Release all waiting consumers
                with self.consumerCondition:
                    self.consumerCondition.notify_all()
                self.condition.notify_all()

            else:
                # Mark this consumer as having read
                self.waitList.append(current_thread())
                self.condition.notify_all()

            return self.data


class Producer(Thread):
    """Represents a producer."""

    def __init__(self, cell, accessCount, sleepMax):
        Thread.__init__(self, name="Producer")
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        print(f"{self.name} starting up\n")
        for count in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            self.cell.setData(count + 1)
        print(f"{self.name} is done producing\n")


class Consumer(Thread):
    """Represents a consumer."""

    def __init__(self, name, cell, accessCount, sleepMax):
        Thread.__init__(self, name="Consumer " + name)
        self.accessCount = accessCount
        self.cell = cell
        self.sleepMax = sleepMax

    def run(self):
        print(f"{self.name} starting up\n")
        for i in range(self.accessCount):
            time.sleep(random.randint(1, self.sleepMax))
            self.cell.getData()
        print(f"{self.name} is done consuming\n")


def main():
    numConsumers = int(input("Enter the number of consumers: "))
    accessCount = int(input("Enter the number of accesses: "))

    cell = SharedCell(numConsumers)
    p = Producer(cell, accessCount, 4)

    consumers = [
        Consumer(str(i), cell, accessCount, 4)
        for i in range(numConsumers)
    ]

    print("Starting the threads\n")

    p.start()
    for c in consumers:
        c.start()


if __name__ == "__main__":
    main()
