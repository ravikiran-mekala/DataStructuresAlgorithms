"""Insert at Tail
   Explanation: Traverse to end and link new node.
   Example: 1→2, insert 3 → 1→2→3
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    tail = None
    for v in values:
        new_node = Node(v)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head


def list_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


# TC: O(N), SC: O(1)
def insert_at_end(head, node):
    if not head:
        return node
    temp_head = head
    while head.next:
        head = head.next
    head.next = node
    return temp_head


# Dry runs / examples
# 1) Insert into empty list
head = None
head = insert_at_end(head, Node(1))
print(list_values(head))  # [1]

# 2) Insert into existing list [1,2] → insert 3
head = build_list([1, 2])
head = insert_at_end(head, Node(3))
print(list_values(head))  # [1, 2, 3]

# 3) Single element list [10] → insert 20
head = build_list([10])
head = insert_at_end(head, Node(20))
print(list_values(head))  # [10, 20]

# 4) Multiple inserts on initially empty list
head = None
head = insert_at_end(head, Node(5))
head = insert_at_end(head, Node(6))
head = insert_at_end(head, Node(7))
print(list_values(head))  # [5, 6, 7]
