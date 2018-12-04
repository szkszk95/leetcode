### 正则表达式的一些题目

#### 44. Wildcard Matching
##### 模糊匹配，"?"代表一个单独字符，"*"代表任意长度（可为0）的字符。判断字符串是否能够匹配

样例：
```
Example:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```
方法一：回溯法，但是会超时
```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # print(s, p)
        if not p:
            return True if not s else False
        
        if s and (p[0] == '?' or p[0] == s[0]):
            return self.isMatch(s[1:], p[1:])
        elif p[0] != '*':
            return False
        
        while s and p[0] == '*':
            # print("-->", s, p)
            if self.isMatch(s, p[1:]):
                return True
            s = s[1:]
            
        return self.isMatch(s, p[1:])
```
方法二：动态规划，假设s，p长度为m，n

利用一个状态数组存储匹配状态，dp[i][j]代表s[:i]与p[:j]是否匹配。首先初始化全为False，然后：

1. dp[0][0]=True
2. 对于以开头连续的"*"，dp[0][j]=True
3. 若s[i]==p[j]或p[j]="?"，则等于之前的匹配状态
4. 若p[j]=="*"，则等于s或p向前推进一个，dp[i][j-1]对应*代表空的情况，dp[i-1][j]代表之后的递推，即*代表之后的所有字符

```python
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
```










