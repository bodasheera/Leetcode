# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
       
        stack = []
        stack.append(root)
        visited = set()
        res = []

        while stack:

            node = stack.pop()

            if node and node not in visited:

                if node.right:
                    stack.append(node.right)

                stack.append(node)

                if node.left:
                    stack.append(node.left)


                visited.add(node)

            elif node:
                res.append(node.val)

        return res



    def inorderTraversalDFS(self, root: Optional[TreeNode]) -> List[int]:
       
        def solve(root, res):

            if root == None:
                return 

            solve(root.left, res)
            res.append(root.val)
            solve(root.right, res)

            return 

        res = []

        solve(root, res)

        return res

