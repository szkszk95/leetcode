## Jump Game
### 给定一个数组，每个位置上的数字表示在这个位置上最多能跳几步

#### 55.Jump Game 给定数组,问能否走到终点

思路：从前往后找i+nums[i]为最大能走到的位置
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

从后往前依次往前找能够到最后一个点的点，看能不能让最后一个点找回0
```python
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if (i + nums[i] >= lastPos):
                lastPos = i
        return lastPos == 0
```

#### 45.Jump2，若保证一个数组能够跳到最后一个点，找其最短的路径需要走多少步
贪心算法，每一步找i+nums[i],与55题第一种思路一致
