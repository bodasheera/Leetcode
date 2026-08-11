# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = float('-inf')

        def solve(node):

            if node is None:
                return 0

            # hypothesis
            left = max(0 , solve(node.left))
            right = max(0, solve(node.right))

            self.max_sum = max(self.max_sum, node.val + left + right)

            # induction
            return node.val + max( left , right )

        solve(root)
        return self.max_sum
            