"""
Stack using Queues
"""


class Queue:
    def __init__(self, arr=None):
        self.arr = arr or []
        self.size = len(self.arr)

    def push(self, num):
        """Add an element to the rear of the queue"""
        self.arr.append(num)
        self.size += 1

    def pop(self):
        """Remove and return the front element of the queue"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        self.size -= 1
        return self.arr.pop(0)

    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        return self.arr[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return self.size == 0

    def get_size(self):
        """Return the current size of the queue"""
        return self.size


class StackUsingQueue:
    def __init__(self) -> None:
        self.queue = Queue()

    def push(self, value):
        """Push value onto the stack in O(n) by rotating the queue"""
        # Enqueue new element
        self.queue.push(value)
        # Rotate the previous elements to move the new one to the front
        rotations = self.queue.get_size() - 1
        for _ in range(rotations):
            self.queue.push(self.queue.pop())

    def pop(self):
        """Remove and return the top element of the stack in O(1)"""
        if self.queue.is_empty():
            raise ValueError("Stack is Empty")
        return self.queue.pop()

    def peek(self):
        """Return the top element without removing it in O(1)"""
        if self.queue.is_empty():
            raise ValueError("Stack is Empty")
        return self.queue.peek()

    def is_empty(self):
        """Return True if the stack is empty"""
        return self.queue.is_empty()

    def size(self):
        """Return the number of elements in the stack"""
        return self.queue.get_size()
