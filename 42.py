# from left-> <-right
# two pointer

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left,right = 0, len(height)-1
        maxleft , maxright= 0,0
        ret = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] < maxleft:
                    ret += maxleft - height[left]
                else:
                    maxleft = height[left]
                left += 1

            else:
                if height[right] < maxright:
                    ret += maxright - height[right]
                else:
                    maxright = height[right]
                right -= 1

        return ret
