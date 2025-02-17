# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        left = head
        right = head
        for _ in range(n):
            right = right.next

        if right is None:
            return head.next

        while right.next is not None:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return head