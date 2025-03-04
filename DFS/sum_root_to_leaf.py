# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node, path_number):
            nonlocal res

            if not node:
                return

            path_number = path_number * 10 + node.val

            if not node.left and not node.right:
                res += path_number

            dfs(node.left, path_number)
            dfs(node.right, path_number)

        dfs(root, 0)
        return res