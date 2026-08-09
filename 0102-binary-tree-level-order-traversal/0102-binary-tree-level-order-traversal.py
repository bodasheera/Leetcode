# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        res = []

        def dfs(root, level):

            if root == None:
                return

            if len(res) == level:
                res.append([])

            # add current ele
            res[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

            return 

        dfs(root, 0)

        return res

    def levelOrder2pass(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # get height of the tree

        def height(root):

            if root == None:
                return 0 

            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        h = height(root)

        # make a array of size h
        res = []
        for _ in range(h):
            res.append([])

        def dfs(root, level):

            if root == None:
                return

            # add current ele
            res[level].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

            return 

        dfs(root, 0)

        return res
