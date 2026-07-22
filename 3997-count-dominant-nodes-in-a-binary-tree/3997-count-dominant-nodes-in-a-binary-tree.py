# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ct = 0
        
    def countDominantNodes(self, root: TreeNode | None) -> int:

        
        def solve(root):

            # base case
            # root is always dominant
            if root is None:
                return float('-inf')

            # hypothesis
            mx = max (solve(root.left), solve(root.right))

            # induction
            if root.val >= mx:
                self.ct += 1
    
            return max(mx, root.val)

        solve(root)
        return self.ct
        
        