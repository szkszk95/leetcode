# EASY PROBLEM

主要整理一下做的一些比较简单却没有找到最优解或者最美代码解的一些题目

## 922. Sort Array By Parity II
给你一个数组，让第奇数个位置上的数都是奇数，偶数位置上的都是偶数。
```
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
```

第一反应解---暴力：   
```python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 0
        res = [0 for _ in A]
        
        for a in A:
            if a % 2 == 0:
                res[2*j] = a
                j += 1 
            else:
                res[2*i+1] = a
                i += 1
        return res
```

优美解：  
遍历偶数index的元素，并且找到奇数时与下一个在奇数点的偶数互换  
- 不用额外的空间
- O(n)

```python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
```

## 925. Long Pressed Name
有人打字打自己的名字，键盘每个键都可能是坏的，可能会按很多下，判断打出来的字是不是真正的名字，也就是说如果重复了就认为可能是只按了一次，算对。  
```
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
```

我的解---暴力解，试图将所有的情况考虑到，似乎并不简洁
```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name):
            return False
        self.typed = typed
        c, n = "", 0
        for i in range(len(name)):
            if c != name[i]:
                if not self.findNextChar(c, n):
                    return False
                c = name[i]
                n = 1
            else:
                n += 1
        return self.findNextChar(c, n)
            
    def findNextChar(self, char, times):
        for i in range(times):
            if len(self.typed) > 0 and self.typed[0] == char:
                self.typed = self.typed[1:]
            else:
                return False
        while len(self.typed) > 0 and self.typed[0] == char:
            self.typed = self.typed[1:]
        return True
```

优美解：遍历打出来的字符串，然后若与name字符串一致则name往后跳，如果不一致且与前面的typed不一样，则说明打错了，终止，反之typed往后走一格。最后，如果typed遍历结束时name也遍历结束，则说明匹配。
```python
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        
        for j in range(len(typed)):
            if i < len(name) and typed[j] == name[i]:
                i+=1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            
        return i == len(name)
```

