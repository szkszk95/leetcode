# the TLE solution of 3 sum problem
# using l-> i <-r but the TIME cost is not best 
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        res = []
        nums = sorted(nums)
        # print(nums)
        for i in range(1, len(nums)-1):
            l = 0
            r = len(nums) - 1
            while l < i and r > i:
                result = nums[l] + nums[i] + nums[r]
                # print("{}+'{}'+{}={}:{}".format(nums[l], nums[i], nums[r], result, i))
                if nums[l] > 0:
                    break
                if result == 0:
                    if [nums[l], nums[i], nums[r]] not in res:
                        res.append([nums[l], nums[i], nums[r]])
                    while nums[l] + nums[i] + nums[r] == 0:
                        if l < i-1:
                            l += 1
                        elif r > i+1:
                            r -= 1
                        else:
                            l += 1
                            r -= 1
                            break
                elif result < 0:
                    l += 1
                elif result > 0:
                    r -= 1
        return res
