# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque[root]

        while queue:
            Node = queue.popleft()
            if Node.left:
                Node.left = Node.right
            if Node.right:
                Node.right = Node.left
            
        return root