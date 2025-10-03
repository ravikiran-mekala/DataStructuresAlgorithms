"""
Nth Node from End (1-based)
   Explanation: Two pointers offset by n.
   Example: [1,2,3,4,5], n=2 → 4
"""

# TC: O(N), SC: O(1)


def nth_from_end(head, n):
    # Guard against non-positive n (1-based indexing)
    if n <= 0:
        return None
    if not head:
        return head
    left, right = head, head
    cnt = n
    while cnt and right:
        right = right.next
        cnt -= 1
    # Case where n > length of the ll
    if cnt:
        return None

    while right:
        right = right.next
        left = left.next

    return left
