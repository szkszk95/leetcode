# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        temp = head
        empty = []
        l = len(lists)
        m_v = None
        while len(empty) != l:
            # print(empty)
            m_i = -1
            for i in range(l):
                if lists[i] == None:
                    if i not in empty:
                        empty.append(i)
                    continue
                if m_i == -1:
                    m_i = i
                    m_v = lists[i].val
                if lists[i].val < m_v:
                    m_v = lists[i].val
                    m_i = i
            if m_i == -1:
                break
            # print("min", m_v, m_i)
            lists[m_i] = lists[m_i].next
            temp.next = ListNode(m_v)
            temp = temp.next
        return head.next
        
