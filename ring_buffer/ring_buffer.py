class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def __str__(self):
        return f"Buffer: {self.storage}"

    def append(self, item):
        if self.current == len(self.storage):
            self.current = 0
            self.storage[self.current] = item
            self.current += 1
        else:
            self.storage[self.current] = item
            self.current += 1

    def get(self):
        return [i for i in self.storage if i is not None]
