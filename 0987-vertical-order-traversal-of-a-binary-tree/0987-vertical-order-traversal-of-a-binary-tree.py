# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        col_map = defaultdict(list)

        def solve(root, row , col):

            # base case
            if root == None:
                return
                

            # hypothesis
            solve(root.left,row + 1, col - 1)

            col_map[col].append([row, root.val])


            solve(root.right, row + 1, col + 1)

        solve(root, 0, 0)
        print(col_map)

        res = []
        for keys in sorted(col_map.keys()):

            # sort by row and then values as per the question
            # sorting in place
            col_map[keys].sort(key = lambda x: (x[0], x[1]))

            temp = []

            # now add all the values in res
            for val in col_map[keys]:
                temp.append(val[1])

            res.append(temp)

        return res