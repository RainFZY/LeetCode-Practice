#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
# 法一
# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         if n < 1:
#             return []
#         self.result = []
#         # 之前的皇后占的位置攻击的范围（新的不能占）
#         self.cols = set()
#         self.pie = set()
#         self.na = set()

#         self.DFS(n, 0, [])
#         return self.generate_result(n)

#     def DFS(self, n, row, cur_state):
#         # termainator
#         if row >= n:
#             self.result.append(cur_state)
#             return 
#         # current level
#         for col in range(n):
#             # 与之前的冲突，跳过本次循环
#             if col in self.cols or row + col in self.pie or row - col in self.na:
#                 continue
#             # 没有冲突，更新攻击范围
#             self.cols.add(col)
#             self.pie.add(row + col)
#             self.na.add(row - col)
#             # drill down
#             self.DFS(n, row + 1, cur_state + [col])
#             # 回溯
#             self.cols.remove(col)
#             self.pie.remove(row + col)
#             self.na.remove(row - col)
    
#     # 画棋盘你，这个不是重点
#     def generate_result(self, n):
#         board = []
#         for res in self.result:
#             for i in res:
#                 board.append("." * i + "Q" + "." * (n - i -1))
#         return [board[i: i + n] for i in range(0, len(board), n)]

# 法二
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 用来最后画图
        res = []
        def DFS(cols, pie, na):
            row = len(cols)
            if row == n:
                res.append(cols)
                return
            for col in range(n):
                if col not in cols and row + col not in pie and row - col not in na:
                    DFS(cols + [col], pie + [row + col], na + [row - col])
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res] 
# @lc code=end

