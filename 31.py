# find the place nned to change
# replace it with the min number greater than fore number
# then put the next min number

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                r = i-1
                break
        if r == -1:
            nums = nums.reverse()
        else:
            num = nums[r]
            candidates = nums[r:].copy()
            # find the min number greater than fore number
            temp = [i for i in nums[r+1:] if i > nums[r]]
            nums[r] = min(temp)
            candidates.remove(nums[r])
            r += 1
            while len(candidates) > 0 and r < len(nums):
                nums[r] = min(candidates)
                candidates.remove(nums[r])
                r += 1
