#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
# 一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2
# 如果超过，就没有约束作用了，相当于 k = +infinity
# 根据123的法一改写，调整max_k大小即可
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        max_k = k
        n = len(prices)
        # 如果不加会出现超内存的错误，因为传入的 k 值会非常大，dp 数组太大了
        if max_k > n / 2:
            return self.maxProfit_k_inf(prices)
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(0, n):
            for k in range(max_k, 0, -1):
                # base case
                if i == 0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]
                    continue

                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[n-1][max_k][0]
    
    # k=+inf的情况，直接把122中的解抄过来
    def maxProfit_k_inf(self, prices: List[int]) -> int:
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

