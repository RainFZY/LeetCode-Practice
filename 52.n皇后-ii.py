#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
# 跟 51 几乎一样
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        return len(res)
# @lc code=end

