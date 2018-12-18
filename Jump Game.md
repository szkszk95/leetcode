## 55. Jump Game

给出一个列表，从第一格开始跳，每一个元素代表最多能跳几格，问最后能不能跳到最后。

```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

```python
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 0
        if len(nums) <= 1:
            return True
        while nums[cur]+cur < len(nums)-1:
            temp = 0
            jump = 0
            if nums[cur] == 0:
                return False
            for i in range(nums[cur]):
                this = nums[cur+i+1]+i+1
                if i == 0:
                    temp = this
                    jump = 1
                elif this > temp:
                    jump = i+1
                    temp = this
            cur += jump
        return True
```

## 45. Jump Game II

给出一个列表，从第一格开始跳，每一个元素代表最多能跳几格，问跳到最后需要多少步。  

贪心算法，每次选能跳的最远的，max(i+jump[i])  

```
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
```
