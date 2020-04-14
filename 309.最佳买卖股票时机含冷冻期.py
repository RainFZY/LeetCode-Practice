#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for i in range(n)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
            # 第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 
            dp[i][1] = max(dp[i - 2][0] - prices[i], dp[i - 1][1])
        return dp[n - 1][0]
# @lc code=end

