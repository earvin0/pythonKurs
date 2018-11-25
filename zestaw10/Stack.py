class Stack:
    def __init__(self, size=10):
        self.items = size * [None]
        self.n = 0
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stack is full!")
        self.items[self.n] = data
        self.n = self.n + 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty!")
        self.n = self.n - 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data