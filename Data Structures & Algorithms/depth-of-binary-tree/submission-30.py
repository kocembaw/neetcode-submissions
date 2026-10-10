# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        max_depth = 0
        while queue:
            node = deque.popleft()
            if node:
                
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            max_depth += 1
        return max_depth                
