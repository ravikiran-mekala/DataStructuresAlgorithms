"""Same Tree
   Explanation: Compare structure and values.
   Example: T1=[1,2,3], T2=[1,2,3] → true
"""

def same_tree(r1, r2) -> bool:
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False
    if r1.val != r2.val:
        return False
    
    return same_tree(r1.left, r2.left) and same_tree(r1.right, r2.right)
