# do not check the res when append, cost too much time
# if the index [i] is the same to the one before
# jump to next
# i, l-> , <-r
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        res = []
        nums = sorted(nums)
        # print(nums)
        for i in range(0, len(nums)-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                result = nums[i] + nums[l] + nums[r]
                if result == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    temp_l, temp_r = nums[l], nums[r]
                    while l<r and nums[l] == temp_l:
                        l += 1
                    while l<r and nums[r] == temp_r:
                        r -= 1
                elif result < 0:
                    l += 1
                else:
                    r -= 1
        return res
