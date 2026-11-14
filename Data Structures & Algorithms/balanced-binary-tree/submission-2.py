# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        left = 0
        right = 0

        def height(node):
            if not node:
                return 0

            nonlocal left, right

            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)
        
        height(root)
        if abs(left - right) <= 1:
            return True
        return False