# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        avg = []
        q = deque()
        q.append(root)

        while q:

            qlen = len(q)
            total = 0
            
            for _ in range(qlen):

                node = q.popleft()
                total += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            avg.append(total / qlen)

        return avg





    def averageOfLevelsDFS(self, root: Optional[TreeNode]) -> List[float]:
        

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

