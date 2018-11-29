### 与矩形，直方图有关的题目

#### 84. Largest Rectangle in Histogram
#### 寻找直方图中最大的矩形

思路：通过栈，形成一个递增的栈，，并且栈中记录的是元素的位置。碰到比栈底大的元素就进栈，比栈底小的元素就执行求解操作。

求解过程为：首先，在数组的尾部添加一个0元素处理最后未弹出的栈元素，在遇到小于栈底元素的值时进行：

（1）记录并且弹出栈底元素作为矩形的高
（2）计算当前栈底与当前位置的差作为矩形的低
（3）直到栈底比当前元素小，压入当前元素继续往后遍历

```python
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        result = 0
        heights.append(0)
        while i < len(heights):
            if len(stack) == 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                num = stack.pop(-1)
                # 若弹出成空栈则宽度为当前位置
                result = max(result,heights[num]*(i-stack[-1]-1 if stack else i))
        return result           
```


#### 85. Maximal Rectangle
#### 寻找一个矩阵中最大的由“1”组成的矩阵

思路：统计每一个位置的元素上面连着的有多少个1，然后在这一行往前遍历，那么这个矩阵的高度为最小的高度元素，长度为到底的长度，直到到头或者到0为止
```
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
```
记为：
```
[
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0], 
    [0, 2, 0, 2, 1, 1], 
    [0, 3, 1, 3, 2, 2], 
    [0, 4, 0, 0, 3, 0]
]
```
```python
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        result = 0
        m, n = len(matrix), len(matrix[0])
        table = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == "1":
                    # 根据上一行的大小+1
                    table[i][j] = table[i-1][j] + 1
                    col = j
                    l = table[i][j]
                    # 往前遍历
                    while col >=0 and table[i][col] != 0:
                        # 取已有高度的最小值
                        l = min(l, table[i][col])
                        # 乘以到头的距离
                        temp = l*(j-col+1)
                        result = max(result, temp)
                        col -= 1
        # print(table)
        return result
```


