#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# 法一：暴力解法，会超时
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 res = max(res, prices[j] - prices[i])
#         return res

# 法二：一次遍历求最大差
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         minPrice = float('inf')
#         res = 0
#         for i in range(len(prices)):
#             minPrice = min(minPrice, prices[i])
#             res = max(res, prices[i] - minPrice)
#         return res


# 法三：动态规划，dp[i]=max(0,dp[i−1])，每一步都取最优
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         diff = 0
#         res = 0
#         for i in range(1, len(prices)):
#             diff = max(0, diff + prices[i] - prices[i - 1])
#             res = max(res, diff)
#         return res

# DP，一种方法团灭股票问题
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
# base case：
# dp[-1][k][0] = dp[i][0][0] = 0
# dp[-1][k][1] = dp[i][0][1] = -infinity
# 状态转移方程：
# 三种状态（三维）：i：天数，k：最大交易次数限制，1持有状态0未持有状态
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# 本题 k=1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for i in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 因为只能买一次，i天买的话，dp[i - 1][0]必为0
            dp[i][1] = max(dp[i - 1][1], 0 - prices[i])
        # 最后一天必须卖出，这样才能受益最大
        return dp[n - 1][0]

# 节省空间复杂度的改进方法
# 用两个变量不断更新，取代用二维数组记录所有状态
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0
#         n = len(prices)
#         dp_i_0, dp_i_1 = 0, -prices[0]
#         for i in range(1, n):
#             dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
#             # 因为只能买一次，i天买的话，dp[i - 1][0]必为0
#             dp_i_1 = max(dp_i_1, 0 - prices[i])
#         # 最后一天必须卖出，这样才能受益最大
#         return dp_i_0



# @lc code=end

