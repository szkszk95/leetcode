class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = False
        a = -1
        b = -1
        for i in range(len(nums)):
            if checked:
                if nums[i] != target:
                    b = i-1
                    return [a, b]
                if i == len(nums)-1:
                    return [a, i]
            else:
                if nums[i] == target:
                    a = i
                    b = i
                    checked = True
        return [a, b]
