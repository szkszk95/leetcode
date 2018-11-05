# change the direction of the arrows


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k<2:
            return head
        
        ret = head
        for i in range(k-1):
            ret = ret.next
            if ret is None:
                return head
            
        prev, current = None, head
        for i in range(k):
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        
        head.next = self.reverseKGroup(current, k)
        return ret
