"""Detect a Cycle
   Explanation: Floyd’s tortoise-hare algorithm.
   Example: 1→2→3→4→2 → cycle
"""

"""
Base Cases: empty ll, acyclic ll, ll with even / odd nodes cycle.
"""


def detect_cycle(head) -> bool:
    # Standard Floyd's cycle detection
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # We are using 'is' instead '==' as someone can rewrite __eq__ magic method to
        # compare node with their values. Hence 'is' is a safer bet.
        if slow is fast:
            return True
    return False
