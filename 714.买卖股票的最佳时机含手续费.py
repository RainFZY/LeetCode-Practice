#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0] - fee
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[n - 1][0]
        
# @lc code=end

