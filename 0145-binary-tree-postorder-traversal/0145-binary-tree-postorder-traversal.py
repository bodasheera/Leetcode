# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Basically do preorder with a twist and return reverse

        if not root:
            return []

        stack = []
        res = []

        stack.append(root)

        while stack:

            top = stack.pop()
            res.append(top.val)

            if top.left:
                stack.append(top.left)

            if top.right:
                stack.append(top.right)
        
        return res[::-1]


    def postorderTraversalBFS(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
       
        stack = []
        stack.append(root)
        visited = set()
        res = []

        while stack:

            node = stack.pop()

            if node not in visited:

                stack.append(node)

                if node.right:
                    stack.append(node.right)


                if node.left:
                    stack.append(node.left)


                visited.add(node)

            else:
                res.append(node.val)

        return res

    def postorderTraversalDFS(self, root: Optional[TreeNode]) -> List[int]:
       
        def solve(root, res):

            if root == None:
                return 

            solve(root.left, res)
            solve(root.right, res)
            res.append(root.val)

            return 

        res = []

        solve(root, res)

        return res

