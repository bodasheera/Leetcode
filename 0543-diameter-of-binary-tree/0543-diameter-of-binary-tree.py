# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        total_nodes = [0]

        def height(node, total_nodes):

            # base case
            if node is None:
                return 0

            # hypothesis
            left = height(node.left, total_nodes)
            right = height(node.right, total_nodes)

            total_nodes[0] = max(total_nodes[0] , 1 + left + right)

            # induction
            return 1 + max(left, right)

        height(root, total_nodes)

        return total_nodes[0] - 1

