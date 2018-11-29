#### 89. Gray Code
#### 给定一个n，长度为n的所有二进制数，并且两两之间只有一个位不同

##### 1. 从二进制字符串的角度，从[0,1]开始，每次逆序复制，前半段头加0，后半段头加1（下面代码是从n=2开始的）

(56ms)

```python
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        string = ["00", "01", "11", "10"]
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]

        for i in range(2, n):
            next_half = string.copy()[::-1]
            for j in range(len(string)):
                string[j] = "0"+string[j]
                next_half[j] = "1"+next_half[j]
            string = string + next_half

        string = [int(s, 2) for s in string]
        return string
```

##### 2. 从数字的角度，从[0,1]开始，每次逆序，加上2的n次方, 其实跟动态规划思路一样的甚至不用递归，可能逆序的时候比较慢

(40ms)

```python
class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        string = [0, 1]
        if n == 0:
            return [0]


        for i in range(1, n):
            next_half = string.copy()[::-1]
            num = 2**i
            for j in range(len(string)):
                next_half[j] = next_half[j]+num
            string = string + next_half
        return string
```
