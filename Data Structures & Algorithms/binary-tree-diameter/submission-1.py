# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node: TreeNode | None) -> int:
            nonlocal diameter
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            # najdłuższa ścieżka przechodząca przez ten węzeł
            diameter = max(diameter, left + right)
            # wysokość tego poddrzewa (w węzłach)
            return 1 + max(left, right)

        height(root)
        return diameter