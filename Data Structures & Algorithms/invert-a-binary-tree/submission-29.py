# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]

        for i in range(len(root)):

            node = stack.pop()

            if node.left:
                node.left = node.right
            if node.right:
                node.right = node.left
            stack.append(node)
        
        return root