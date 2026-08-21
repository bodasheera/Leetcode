# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def solve(root, total):

            # base case
            if root is None:
                return False
            

            # base case leaf node
            if not root.left and not root.right:
                return total == root.val

            total = total - root.val

            # hypothesis
            left = solve(root.left  , total)
            right = solve(root.right , total)

            return left or right
        

        def solve1(root, current_sum):

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


        # return solve1(root, 0)
        return solve(root, targetSum)