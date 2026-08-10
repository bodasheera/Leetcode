# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        level = 0

        q = deque()

        q.append(root)

        while q:

            qlen = len(q)
            res.append([])

            for _ in range(qlen):

                # add all nodes in a level in our res
                node = q.popleft()
                res[level].append(node.val)

                # add children back in q
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return res[::-1]





    def levelOrderBottomDFS(self, root: Optional[TreeNode]) -> List[List[int]]:

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

