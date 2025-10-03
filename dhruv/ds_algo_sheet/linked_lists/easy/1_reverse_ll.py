"""
Reverse a Linked List
   Explanation: Iteratively flip next pointers.
   Example: 1→2→3→4 → 4→3→2→1
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def list_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values

# TC: O(N), SC: O(1)


def reverse_ll(head):
    prev, new_head = None, None
    while head:
        prev = head
        head = head.next
        prev.next = new_head
        new_head = prev
    return new_head


# Dry runs / examples
# 1) Empty list
head = None
print(list_values(reverse_ll(head)))  # []

# 2) Single element
head = build_list([1])
print(list_values(reverse_ll(head)))  # [1]

# 3) Two elements
head = build_list([1, 2])
print(list_values(reverse_ll(head)))  # [2, 1]

# 4) Multiple elements
head = build_list([1, 2, 3, 4])
print(list_values(reverse_ll(head)))  # [4, 3, 2, 1]

# 5) Duplicates
head = build_list([1, 1, 2, 2, 3])
print(list_values(reverse_ll(head)))  # [3, 2, 2, 1, 1]

# 6) Mixed/negative values
head = build_list([0, -1, 2, -3])
print(list_values(reverse_ll(head)))  # [-3, 2, -1, 0]

if __name__ == "__main__":
    pass
