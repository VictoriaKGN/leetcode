# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        def dfs(node, path, curr_sum):
            if not node:
                return
            
            path.append(node.val)
            curr_sum += node.val

            if not node.left and not node.right and curr_sum == targetSum:
                res.append(list(path))

            dfs(node.left, path, curr_sum)
            dfs(node.right, path, curr_sum)

            path.pop()

        dfs(root, [], 0)

        return res
