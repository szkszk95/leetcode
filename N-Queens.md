### N-Queens

N皇后是一种经典的回溯问题，其重要的解题思路是选择回溯的状态以及状态之间的转移关系

#### 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.  
给出一个NxN格的棋盘，返回所有的N皇后的解

```python
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.res = []
        self.run([], 0)
        return self.res
    
    # 用于判断是否满足皇后之间不能攻击的条件
    def valid(self, queens, x, y):
        # print("-->", queens, x, y)
        for q in queens:
            q_x, q_y = q
            if q_x == x or q_y == y or abs(q_x-x)==abs(q_y-y):
                return False
        return True
        
    # 回溯的主函数，按行推进
    def run(self, queens, row):
        # 如果所有行填满，则生成对应的table，并且加入结果之后，回退
        if len(queens) == self.n:
            table = [["." for i in range(self.n)] for j in range(self.n)]
            for q in queens:
                x, y = q
                table[x][y] = "Q"
            for i in range(self.n):
                table[i] = "".join(table[i])
            self.res.append(table)
            return
        
        # 尝试在该行的每一个位置放置一个皇后，若满足要求，则往下一行推进
        for i in range(self.n):
            if self.valid(queens, row, i):
                self.run(queens+[[row, i]], row+1)
```
