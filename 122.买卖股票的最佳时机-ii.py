#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
# 贪心算法
# 遍历price，策略是所有上涨交易日都买卖（赚到所有利润，且不限买卖次数）
# 所有下降交易日都不买卖（永不亏钱）
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                profit += (prices[i + 1] - prices[i])
        return profit
# @lc code=end

