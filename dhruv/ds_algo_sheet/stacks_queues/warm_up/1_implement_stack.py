"""
Implement Stack
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
