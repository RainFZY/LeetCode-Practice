#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
# 贪心算法
# 遍历price，策略是所有上涨交易日都买卖（赚到所有利润，且不限买卖次数）
# 所有下降交易日都不买卖（永不亏钱）
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         for i in range(len(prices) - 1):
#             if prices[i + 1] > prices[i]:
#                 profit += (prices[i + 1] - prices[i])
#         return profit

# DP，一种方法团灭股票问题
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
# 状态转移方程：
# 三种状态：i：天数，k：最大交易次数限制，1持有0未持有
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# 本题 k=+inf
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         n = len(prices)
#         dp = [[0] * 2 for i in range(n)]
#         dp[0][0], dp[0][1] = 0, -prices[0]
#         for i in range(1, n):
#             dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
#             dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
#         # 最后一天必须卖出，这样才能受益最大
#         return dp[n - 1][0]

# 节省空间复杂度的改进方法
# 用两个变量不断更新，取代用二维数组记录所有状态
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # 因为只能买一次，i天买的话，dp[i - 1][0]必为0
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        # 最后一天必须卖出，这样才能受益最大
        return dp_i_0
# @lc code=end

