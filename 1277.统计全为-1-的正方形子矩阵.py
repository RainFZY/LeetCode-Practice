#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#

# @lc code=start
# 类似 221
# dp[i][j]=x，表示以(i,j)​​​为右下角的正方形的最大边长为x，
# 也表示以(i,j)​​​为右下角的正方形的数量 (关键！)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    cnt += dp[i][j]
        return cnt
# @lc code=end

