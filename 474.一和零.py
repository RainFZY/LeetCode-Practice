#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
# DP
# 把总共的 0 和 1 的个数视为背包的容量，每一个字符串视为装进背包的物品
# 这道题就可以使用 0-1 背包问题的思路完成，这里的目标值是能放进背包的字符串的数量
# 由于容量、重量有两个维度值，所以需要二维dp table
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(len(strs)):
            zeros = strs[i].count('0')
            ones = strs[i].count('1')
            # 更新j>zeros, k>ones的部分
            for j in range(m, zeros-1, -1):
                for k in range(n, ones-1, -1):
                    dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones] + 1)
        return dp[-1][-1]

# @lc code=end

