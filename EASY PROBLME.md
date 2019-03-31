# EASY PROBLEM

主要整理一下做的一些比较简单却没有找到最优解或者最美代码解的一些题目

922. Sort Array By Parity II
给你一个数组，让第奇数个位置上的数都是奇数，偶数位置上的都是偶数。
"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
"""

第一反应解：   
"""python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 0
        res = [0 for _ in A]
        
        for a in A:
            if a % 2 == 0:
                res[2*j] = a
                j += 1 
            else:
                res[2*i+1] = a
                i += 1
        return res
"""

优美解：  
遍历偶数index的元素，并且找到奇数时与下一个在奇数点的偶数互换  
- 不用额外的空间
- O(n)

"""python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
"""
