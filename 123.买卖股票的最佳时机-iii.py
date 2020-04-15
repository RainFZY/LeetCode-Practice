#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
# max_k = 2
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         max_k = 2
#         n = len(prices)
#         dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
#         for i in range(0, n):
#             for k in range(max_k, 0, -1):
#                 # base case
#                 if i == 0:
#                     dp[0][k][0] = 0
#                     dp[0][k][1] = -prices[0]
#                     continue

#                 dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
#                 dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

#         return dp[n-1][max_k][0]


# 相比法一构建三维数组，这样子大大节省空间
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp_i10 = dp_i20 = 0
        dp_i11 = dp_i21 = -prices[0]
        n = len(prices)
        for i in range(n):
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, -prices[i])
        return dp_i20
# @lc code=end

