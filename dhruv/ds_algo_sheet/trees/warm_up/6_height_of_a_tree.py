"""Height of a Tree
   Explanation: Max depth of left/right + 1.
   Example: [3,9,20,null,null,15,7] → 3
"""

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1