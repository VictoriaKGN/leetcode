# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            queue_size = len(queue)
            level_tail_found = False

            for _ in range(queue_size):
                node = queue.popleft()
                if node:
                    if not level_tail_found:
                        res.append(node.val)
                        level_tail_found = True

                    queue.append(node.right)
                    queue.append(node.left)

        return res