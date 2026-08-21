# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def solve(root, direction):

            if root == None:
                return 0

            # leaf
            elif root.left == None and root.right == None:
                if direction == 'L':
                    return root.val
                else:
                    return 0

            left = solve(root.left, 'L')
            right = solve(root.right, 'R')

            return left + right

        return solve(root, 'C')