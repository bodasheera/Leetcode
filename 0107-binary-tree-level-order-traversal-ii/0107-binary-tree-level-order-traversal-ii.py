# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        
        def solve(root, level):

            # base
            if not root:
                return 

            # induction
            if len(res) == level:
                res.append([])

            res[level].append(root.val)

            # hypothesis
            solve(root.left, level+1)
            solve(root.right, level+1)

        solve(root, 0)

        return res[::-1]

