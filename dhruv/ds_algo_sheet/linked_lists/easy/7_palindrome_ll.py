"""Palindrome Linked List
   
   Example: 1→2→2→1 → true
"""

from node import Node


def check_palindrome(head):
    """
    Check if a linked list is a palindrome.

    Args:
        head: Head node of the linked list

    Returns:
        True if the list is a palindrome, False otherwise
    """
    if not head or not head.next:
        return True

    # Find the middle of the list using slow and fast pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the list.
    # Interesting part is that in odd number of linked list nodes, the middle node would be the
    # last node for both first_half and the second_half. So, there's no need to disconnect the halves.
    # In case of even number of nodes, as the right half ends in None, we would anyways stop the last while loop.
    second_half = reverse_list(slow)

    # Compare first half with reversed second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def reverse_list(head):
    """Helper function to reverse a linked list"""
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev
