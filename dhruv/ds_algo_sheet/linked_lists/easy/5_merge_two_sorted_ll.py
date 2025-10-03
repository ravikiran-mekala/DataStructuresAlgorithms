"""
Merge Two Sorted Lists

   Example: 1→3→5 + 2→4→6 → 1→2→3→4→5→6
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_two_sorted_lists(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    # Create a dummy node to simplify the logic
    dummy = Node(0)  # Assuming Node class exists
    current = dummy

    while head1 and head2:
        if head1.val <= head2.val:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Attach remaining nodes
    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return dummy.next
