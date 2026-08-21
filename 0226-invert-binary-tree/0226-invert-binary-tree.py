# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def solve(root):

            # nothing to invert - base case
            if root is None:
                return None

            # hypothesis
            # assume children are already inverted
            left = solve(root.left)
            right = solve(root.right)

            # induction - swap logic 
            root.left = right
            root.right = left

            return root

        return solve(root)
