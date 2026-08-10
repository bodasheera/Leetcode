# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        

        res = []
        avg = []
        
        def solve(root, level):

            # base
            if not root:
                return 

            # induction
            if len(res) == level:
                res.append([])
                avg.append(0)

            res[level].append(root.val)
            avg[level] = sum(res[level])/ len(res[level])

            # hypothesis
            solve(root.left, level+1)
            solve(root.right, level+1)

        solve(root, 0)

        return avg

