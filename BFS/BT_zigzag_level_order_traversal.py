# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        queue = deque()
        queue.append(root)
        res = []
        zigzag = False

        while queue:
            level = []
            queue_size = len(queue)

            for _ in range(queue_size):
                node = queue.popleft()

                if node:
                    if zigzag:
                        level.insert(0, node.val)
                    else:
                        level.append(node.val)
                    
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                zigzag = not zigzag
                res.append(level)

        return res