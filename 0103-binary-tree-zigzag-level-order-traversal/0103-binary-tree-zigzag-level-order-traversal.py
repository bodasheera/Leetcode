# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        def solve(root, level):

            if root == None:
                return 

            # induction
            if len(res) == level:
                res.append([])

            # even levels normal
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)


            # hypothesis
            solve(root.left, level+1)
            solve(root.right, level+1)


            return 

        solve(root, 0)
        return res
