## 287. Find the Duplicate Number
#### 给定n+1长度的数组，里面仅包含1-n，且仅有一个数字是重复并且会多次出现的，要求找到这个数字

方法一. 哈希
建立一个长度为n的数组记录已经出现过的数
```python
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [-1 for i in range(len(nums))]
        for i, num in enumerate(nums):
            if temp[num] == -1:
                temp[num] = num
            else:
                return num
```
方法二. 二分查找
从n/2开始搜索，小于n/2的数的数量如果大于n/2则重复的数字是在[1, n/2), 相反同理
```python
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums)-1
        while l+1<r:
            # print(l, r)
            mid = int((l+r)/2)
            count = 0
            for num in nums:
                if  l <= num < mid:
                    count += 1
            
            if count > mid-l:
                r = mid
            else:
                l = mid
        count = 0
        for num in nums:
            if num==l:
                count+=1
                if count == 2:
                    return l
        return r
```

方法三. 滚轮法？
