"""Delete a Node (first occurrence)
   Explanation: Bypass the node by linking previous to next.
   Example: 1→2→3, delete 2 → 1→3
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


def delete_node(head, node_val):
    if not head:
        return head
    if head.val == node_val:
        return head.next
    temp_head = head
    while head and head.next:
        if head.next.val == node_val:
            head.next = head.next.next
            break  # delete only first occurrence
        head = head.next
    return temp_head


# Dry runs / examples
# 1) Delete from empty list
head = None
head = delete_node(head, 1)
print(list_values(head))  # []

# 2) Delete head in single-element list [1] → delete 1
head = build_list([1])
head = delete_node(head, 1)
print(list_values(head))  # []

# 3) Delete head in [1,2,3] → delete 1
head = build_list([1, 2, 3])
head = delete_node(head, 1)
print(list_values(head))  # [2, 3]

# 4) Delete middle in [1,2,3] → delete 2
head = build_list([1, 2, 3])
head = delete_node(head, 2)
print(list_values(head))  # [1, 3]

# 5) Delete tail in [1,2,3] → delete 3
head = build_list([1, 2, 3])
head = delete_node(head, 3)
print(list_values(head))  # [1, 2]

# 6) Delete non-existent value → list unchanged
head = build_list([1, 2, 3])
head = delete_node(head, 4)
print(list_values(head))  # [1, 2, 3]

# 7) Delete first occurrence only in [1,2,2,3] → delete 2
head = build_list([1, 2, 2, 3])
head = delete_node(head, 2)
print(list_values(head))  # [1, 2, 3]

# 8) Multiple leading duplicates [2,2,2,3] → delete 2 (first only)
head = build_list([2, 2, 2, 3])
head = delete_node(head, 2)
print(list_values(head))  # [2, 2, 3]
