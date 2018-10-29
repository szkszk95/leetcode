# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such 
# that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms acontainer, such that the 
# container contains the most water.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        max_  = (r-l)*min(height[l], height[r])
        while l<r:
            temp = (r-l)*min(height[l], height[r])
            if temp > max_:
                    max_ = temp
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_
