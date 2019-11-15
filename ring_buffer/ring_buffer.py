class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def __str__(self):
        return f"Buffer: {self.storage}"

    def append(self, item):
        pass

    def get(self):
        return [i for i in self.storage if i is not None]


ring = RingBuffer(3)

print(ring)

print(ring.get())
