"""Insert at Head
   Explanation: Repoint head to new node.
   Example: 2→3, insert 1 → 1→2→3
"""

def insert_at_head(head, insert_node):
    insert_node.next = head
    return insert_node

