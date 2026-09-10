# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.ct = 0

        def solve(root):

            # base case
            if root is None:
                return 0,0

            # hypothesis
            left_sum, left_count = solve(root.left)
            right_sum, right_count = solve(root.right)


            # induction
            avg = (left_sum + right_sum + root.val)//(left_count + right_count + 1)

            if avg == root.val:
                self.ct += 1

            return (left_sum + right_sum + root.val), (left_count + right_count + 1)

        solve(root)

        return self.ct

        



            



