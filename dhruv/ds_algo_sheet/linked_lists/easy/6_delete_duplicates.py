"""Delete Duplicates (Sorted)
   Example: [1,1,2,3,3] → [1,2,3]
"""

from node import Node


def delete_duplicates_sorted(head):
    if not head:
        return None

    temp_head = head

    while head:
        nxt_uni = head.next
        while nxt_uni and head.val == nxt_uni.val:
            nxt_uni = nxt_uni.next

        head.next = nxt_uni
        head = head.next

    return temp_head
