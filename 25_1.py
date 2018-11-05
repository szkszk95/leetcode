# 25. Reverse Nodes in k-Group
# change the list from the begining
# all arrows head to the end

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
        top = ListNode(0)
        top.next = head
        cur = head
        fore = top
        while cur != None:
            temp = []
            for i in range(k):
                temp.append(cur)
                cur = cur.next
                if cur == None:
                    break
            if len(temp) < k:
                return top.next
            fore.next = temp[k-1]
            for i in range(k-1, 0, -1):
                temp[i].next = temp[i-1]
                
            temp[0].next = cur
            fore = temp[0]
            # self.print_(top)
            # print(cur.val, fore.val)
        return top.next
    
    def print_(self, h):
        res = []
        while h != None:
            res.append(h.val)
            h = h.next
        print(res)
