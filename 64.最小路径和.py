#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
# 经典二维 DP
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        for i in range(1, n):
            dp[0][i] += dp[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
# @lc code=end

