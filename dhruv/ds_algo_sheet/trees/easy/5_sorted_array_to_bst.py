"""
Sorted Array to BST
Explanation: Middle as root for balance.
Example: [-10,-3,0,5,9] → balanced BST
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        def create_tree(nums, lo, hi):
            if lo > hi:
                return None
            
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])

            left = create_tree(nums, lo, mid-1)
            right = create_tree(nums, mid+1, hi)

            root.left = left
            root.right = right

            return root
        
        return create_tree(nums, 0, len(nums)-1)
        