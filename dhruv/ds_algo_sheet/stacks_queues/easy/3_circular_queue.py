"""
Circular Queue
   Explanation: Array with wraparound indices.
   Example: Size 3; enqueue 1,2,3; enqueue 4 overwrites/blocks
"""


class CircularQueue:
    def __init__(self, max_size, mode='block'):
        self.q = [0] * max_size
        self.max_size = max_size
        self.size = 0
        if mode not in ['block', 'override']:
            raise ValueError
        self.mode = mode
        self.st = 0
        self.ed = 0

    def push(self, num):
        if self.mode == 'block' and self.size == self.max_size:
            raise Exception
        self.q[self.ed % self.max_size] = num
        self.ed += 1

        if self.mode == 'override' and self.size == self.max_size:
            self.st += 1

        self.size = min(self.size + 1, self.max_size)

    def pop(self):
        if self.size == 0:
            raise Exception
        val = self.q[self.st % self.max_size]
        self.st += 1
        self.size -= 1
        return val

    def peek(self):
        if self.size == 0:
            raise Exception
        return self.q[self.st % self.max_size]
