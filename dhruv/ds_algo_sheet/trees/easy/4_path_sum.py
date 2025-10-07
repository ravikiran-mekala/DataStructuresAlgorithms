"""Path Sum
   Explanation: DFS path with target sum.
   Example: [5,4,8,11,null,13,4,7,2,null,null,null,1], 22 → true
   """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        def checkSum(root, targetSum):
            if root is None:
                if targetSum == 0:
                    return True
                return False
        
            found_left = checkSum(root.left, targetSum-root.val)
            found_right = checkSum(root.right, targetSum-root.val)

            return found_left or found_right
        
        return checkSum(root, targetSum)
