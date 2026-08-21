# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def solve(root, direction , total):

            if root == None:
                return total

            # leaf
            elif root.left == None and root.right == None:
                if direction == 'L':
                    return total + root.val
                else:
                    return total

            left = solve(root.left, 'L', total)
            right = solve(root.right, 'R', total)

            return left + right

        return solve(root, 'C', 0)