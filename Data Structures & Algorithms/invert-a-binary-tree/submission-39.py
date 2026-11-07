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
        
        queue = deque((root))
        

        while queue:
            Node = queue.popleft()
            
            Node.left = Node.right
            Node.right = Node.left
            queue.append(Node.left)
            queue.append(Node.right)
        
        return root

        