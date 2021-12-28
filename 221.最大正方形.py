#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
# DP
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp[i][j]=x，表示以(i,j)​​​为右下角的正方形的最大边长为x
        dp = [[0] * n for _ in range(m)]
        max_side = 0 # 最大正方形的边长
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # border condition
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side ** 2



# @lc code=end

