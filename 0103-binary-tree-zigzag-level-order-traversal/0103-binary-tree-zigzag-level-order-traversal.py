# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
    
        q = deque()

        q.append(root)

        level = 0


        while q:

            # len of all elements in the queue
            qlen = len(q)

            level_nodes = []

            for i in range(qlen):

                node = q.popleft()

                if level % 2 == 0:
                    level_nodes.append(node.val)
                else:
                    level_nodes.insert(0, node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(level_nodes)
            level += 1

        return res


    def zigzagLevelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        
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
