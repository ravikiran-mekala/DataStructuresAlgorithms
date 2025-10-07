"""Symmetric Tree
   Explanation: Mirror check recursively/iteratively.
   Example: [1,2,2,3,4,4,3] → true
"""


class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        return self.are_tree_same(root.left, root.right)

    def are_tree_same(self, root, iroot):
        if root is None and iroot is None:
            return True
        if root is None or iroot is None:
            return False
        if root.val != iroot.val:
            return False

        return self.are_tree_same(root.left, iroot.right) and self.are_tree_same(root.right, iroot.left)
