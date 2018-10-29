# 172. Factorial Trailing Zeroes
# Given an integer n, return the number of trailing zeroes in n!.


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = 0
        i = 5 
        while i<=n:
            nums += int(n/i)
            i = i*5
        return nums
