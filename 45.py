# Greedy
# find the max pos+i to jump

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        
        self.nums = nums
        self.run(0,0)
        return self.res
    
    def run(self, pos, step): 
        # print(pos, step)
        l = self.nums[pos]
        if pos+l+1 >= len(self.nums):
            self.res = step+1
            return 
        
        c_i = 1
        c_s = self.nums[pos+1]+1
    
        for i in range(2, l+1):
            temp = self.nums[pos+i]+i
            if temp > c_s:
                c_s = temp
                c_i = i
        self.run(pos+c_i, step+1)
