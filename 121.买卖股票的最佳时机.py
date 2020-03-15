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
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        res = 0
        for i in range(1, len(prices)):
            diff = max(0, diff + prices[i] - prices[i - 1])
            res = max(res, diff)
        return res

# @lc code=end

