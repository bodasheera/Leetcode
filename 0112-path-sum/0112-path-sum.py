# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if root is None:
            return False
        
        
        def solve(root, current_sum):

            # base case
            if root is None:
                return False

            current_sum = current_sum + root.val

            # leaf node
            if root.left is None and root.right is None:
                return current_sum == targetSum

            # hypotheiss
            left = solve(root.left  , current_sum)
            right = solve(root.right , current_sum)

            # induction
            return left or right 


        return solve(root, 0)