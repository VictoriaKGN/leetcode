# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # def recoverTree(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: None Do not return anything, modify root in-place instead.
    #     """
        
    #     trav = []

    #     def dfs(node):
    #         if not node:
    #             return

    #         dfs(node.left)
    #         trav.append(node)
    #         dfs(node.right)

        
    #     dfs(root)

    #     trav_sorted = sorted(v.val for v in trav)

    #     for i in range(len(trav)):
    #         trav[i].val = trav_sorted[i]
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        first = None
        second = None
        prev = None

        def dfs(node):
            nonlocal first, second, prev

            if not node:
                return

            dfs(node.left)

            if not first and prev and prev.val > node.val:
                first = prev

            if first and prev and prev.val >= node.val:
                second = node

            prev = node

            dfs(node.right)

        
        dfs(root)

        temp = first.val
        first.val = second.val
        second.val = temp