"""
Implement Queue

Note: This implementation uses a list for simplicity, but for better performance,
consider using collections.deque which has O(1) operations for both ends.
"""

from collections import deque


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


class OptimizedQueue:
    """Optimized Queue implementation using collections.deque for O(1) operations"""

    def __init__(self, arr=None):
        self.arr = deque(arr) if arr else deque()
        self.size = len(self.arr)

    def push(self, num):
        """Add an element to the rear of the queue - O(1)"""
        self.arr.append(num)
        self.size += 1

    def pop(self):
        """Remove and return the front element of the queue - O(1)"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        self.size -= 1
        return self.arr.popleft()

    def peek(self):
        """Return the front element without removing it - O(1)"""
        if self.is_empty():
            raise ValueError("Queue is Empty")
        return self.arr[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return self.size == 0

    def get_size(self):
        """Return the current size of the queue"""
        return self.size


def test_queue_implementation(queue_class, name):
    """Test a Queue implementation"""
    print(f"\nTesting {name}:")

    # Test 1: Basic operations
    q = queue_class()
    print(f"Empty queue - is_empty: {q.is_empty()}, size: {q.get_size()}")

    # Test 2: Push operations
    q.push(1)
    q.push(2)
    q.push(3)
    print(
        f"After pushing 1,2,3 - is_empty: {q.is_empty()}, size: {q.get_size()}")
    print(f"Peek: {q.peek()}")

    # Test 3: Pop operations
    print(f"Pop: {q.pop()}")
    print(f"After pop - size: {q.get_size()}, peek: {q.peek()}")

    # Test 4: Multiple pops
    print(f"Pop: {q.pop()}")
    print(f"Pop: {q.pop()}")
    print(f"After all pops - is_empty: {q.is_empty()}, size: {q.get_size()}")

    # Test 5: Pop from empty queue
    try:
        q.pop()
    except ValueError as e:
        print(f"Expected error when popping from empty queue: {e}")

    # Test 6: Peek from empty queue
    try:
        q.peek()
    except ValueError as e:
        print(f"Expected error when peeking from empty queue: {e}")

    # Test 7: Initialize with array
    q2 = queue_class([10, 20, 30])
    print(
        f"Queue initialized with [10,20,30] - size: {q2.get_size()}, peek: {q2.peek()}")


def test_queue():
    """Test both Queue implementations"""
    print("=" * 50)
    print("QUEUE IMPLEMENTATION TESTS")
    print("=" * 50)

    # Test basic Queue implementation
    test_queue_implementation(Queue, "Basic Queue (using list)")

    # Test optimized Queue implementation
    test_queue_implementation(OptimizedQueue, "Optimized Queue (using deque)")

    print("\n" + "=" * 50)
    print("All Queue tests completed!")
    print("=" * 50)


if __name__ == "__main__":
    test_queue()
