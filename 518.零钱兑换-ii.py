#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start
# 二维DP
# dp[i][j]表示使用前i种硬币组成j金额的组合数
# dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
#          = 不用第i枚硬币组合数 + 用i枚硬币组合数
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # base case: 如果金额为0，对多少种硬币来说都是1种方案
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                # 不选当前指标i对应的硬币
                dp[i][j] = dp[i-1][j]
                # 选当前指标i对应的硬币
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[-1][-1]


# 简化 --> 一维DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                # 类似爬楼梯问题，使用这枚硬币，来凑金额i
                dp[i] += dp[i - coin]
        return dp[amount]


        
# @lc code=end

