import random
import timeit


class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1
        self.items = self.n * [None]
        self.head = 0
        self.tail = 0

    def insert(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def remove(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        int_rand = random.randint(self.head, self.tail - 1)
        data = self.items[int_rand]
        self.tail = self.tail - 1
        self.items[int_rand] = self.items[self.tail]
        self.items[self.tail] = None
        if data is None:
            raise OverflowError("rand", int_rand)
        return data

    def is_empty(self):
        return self.tail == self.head

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail


rq = RandomQueue(10)
rq.insert(2)
rq.insert(3)


def test():
    rq.insert(10)
    rq.remove()


print(timeit.Timer('test()',
                   'from __main__ import test, rq')
      .repeat(repeat=1, number=1000000))
