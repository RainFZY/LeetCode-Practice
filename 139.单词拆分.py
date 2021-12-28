#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
# DP
# 转化为是否可以用 wordDict 中的词组合成 s，完全背包问题
# 并且为“考虑排列顺序的完全背包问题”，
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(0, n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
# @lc code=end

