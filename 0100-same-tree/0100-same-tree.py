# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def solve(node1, node2):

            # base case

            if node1 is None and node2 is None:
                return True

            if node1 is None or node2 is None:
                return False

            # hypothesis
            left = solve(node1.left, node2.left)
            right = solve(node1.right , node2.right)

            # induction
            current = node1.val == node2.val

            return current and left and right 

        return solve(p, q)
            

            