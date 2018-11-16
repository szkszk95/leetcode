## 136. single number
### one number once, else two times
思路：进行异或操作，两个一样的数组按位异或后变成0， 最后
```Python
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            res = res^nums[i]
        return res
```




## 137. single number II
### one number once, else three times
思路：保存出现了一次和两次的所有位
```python
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one , two = 0, 0
        for num in nums:
            one = one^num & ~two # 同时要去掉之前出现过两次的那些位
            two = two^num & ~one # 去掉当前确定只出现了一次的位，让two里面的1碰到0保持1，two里面的0碰到1也保持0
        return one
 ```
 
        
 ## 260. single number III
 ### two number once, else three times
 思路：首先进行异或操作去除所有相同的数，得到的结果是两个出现一个的数的异或值Xor。Xor中为1的位数，必定意味着一个数为在这一位上是1，另一个数是0。再遍历一遍数组将所有这一位上是1的数进行异或，得到的一个值为其中一个。再根据Xor即可得到另一个数
 ```Python
 class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = 0
        for num in nums:
            a = a^num
        j = 1
        b = a
        
        # 找到最右边的一个1
        while b >> 1 == b/2:
            b = b>>1
            j = j<<1
        
        # 将所有指定位置为1的数进行异或操作
        t = 0
        for num in nums:
            if num&j:
                t = t^num
        
        t_ = a^t
        return [t, t_]
```
