# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.total_nodes = 0

        def height(node):

            # base case
            if node is None:
                return 0

            # hypothesis
            left = height(node.left)
            right = height(node.right)

            self.total_nodes = max(self.total_nodes , 1 + left + right)

            return 1 + max(left, right)

        height(root)

        return self.total_nodes - 1

