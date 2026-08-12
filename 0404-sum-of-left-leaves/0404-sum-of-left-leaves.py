# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # remove global variable
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:


        def solve(node, left):

            # base case
            if node is None:
                return 0
                
            # base case
            if left and node.left is None and node.right is None:
                return node.val

            # hypothesis
            left = solve(node.left, left = True)
            right = solve(node.right, left = False)

            # induction
            return left + right 
    
        return solve(root, left=False)
        

    def sumOfLeftLeaves1(self, root: Optional[TreeNode]) -> int:
        
        self.sum = 0
        def solve(node, left = False):

            # base case
            if node is None:
                return 0

            if left and node.left is None and node.right is None:
                self.sum += node.val

            # hypothesis
            solve(node.left, left= True)
            solve(node.right, left= False)


        solve(root, left=False)
        return self.sum