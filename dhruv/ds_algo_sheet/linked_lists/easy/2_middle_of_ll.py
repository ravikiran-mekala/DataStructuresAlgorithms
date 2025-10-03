"""Find Middle of List
   Explanation: Slow & fast pointer technique.
   Example: [1,2,3,4,5] → 3
"""

def middle_of_node(head):
    if head is None:
        return head
    s, f = head, head
    while f and f.next and f.next.next:
        s = s.next
        f = f.next.next
    return s.val
