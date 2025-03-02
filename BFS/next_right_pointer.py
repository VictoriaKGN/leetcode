"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        queue = deque()
        queue.append(root)
        res = []

        while queue:
            next_node = None
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()

                if node:
                    node.next = next_node
                    next_node = node
                    queue.append(node.right)
                    queue.append(node.left)

        return root
    
    