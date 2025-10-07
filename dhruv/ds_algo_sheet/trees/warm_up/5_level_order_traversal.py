""" Level Order Traversal
   Explanation: BFS by levels using queue.
   Example: [3,9,20,null,null,15,7] → [[3],[9,20],[15,7]]
"""

from collections import deque

def level_order(root):
    if not root:
        return []
    res = []
    q = deque()

    q.append(root)

    while q:
        size = len(q)
        curr_level = []
        for _ in range(size):
            node = q.popleft()
            curr_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(curr_level)
    
    return res
    
