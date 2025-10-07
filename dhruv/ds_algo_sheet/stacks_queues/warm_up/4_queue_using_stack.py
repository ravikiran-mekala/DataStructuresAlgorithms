"""
Queue using Stacks
   Explanation: Two stacks to simulate FIFO.
   Example: Enqueue 1,2,3; dequeue → 1
   """


class Stack:
    def __init__(self, arr=None):
        self.st = arr or []
        self.size = len(self.st)

    def push(self, num):
        self.st.append(num)

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.st.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.st[-1]

    def is_empty(self) -> bool:
        return len(self.st) == 0

    def size(self) -> int:
        return len(self.st)


class QueueUsingStack:
    def __init__(self) -> None:
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, value):
        """Enqueue: always push into s1"""
        self.s1.push(value)

    def _move_s1_to_s2(self):
        """Move all elements from s1 to s2 to expose the front at s2.top"""
        while not self.s1.is_empty():
            self.s2.push(self.s1.pop())

    def pop(self):
        """Dequeue: return the oldest element"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        if self.s2.is_empty():
            self._move_s1_to_s2()
        return self.s2.pop()

    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            raise ValueError("Queue is empty")
        if self.s2.is_empty():
            self._move_s1_to_s2()
        return self.s2.peek()

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()

    def size(self) -> int:
        return self.s1.size() + self.s2.size()
