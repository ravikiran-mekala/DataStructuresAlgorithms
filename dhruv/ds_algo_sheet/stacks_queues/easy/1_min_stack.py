"""Min Stack
   Explanation: Track current minimum in O(1).
   Example: Push 5,3,7; getMin → 3
"""


class MinStack:
    def __init__(self, arr=None):
        self.st = []  # stores tuples: (value, current_min)
        if arr:
            for v in arr:
                self.push(v)

    def push(self, num):
        if not self.st:
            self.st.append((num, num))
        else:
            self.st.append((num, min(num, self.st[-1][1])))

    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        val, _ = self.st.pop()
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.st[-1][0]

    def is_empty(self) -> bool:
        return len(self.st) == 0

    def size(self) -> int:
        return len(self.st)

    def get_min(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.st[-1][1]
