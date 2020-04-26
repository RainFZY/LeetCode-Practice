#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
# 中心扩散法，共 2n - 1个中心
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if not s:
            return res
        
        def spread(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        for i in range(len(s)):
            odd = spread(i, i)
            even = spread(i, i+1)
            res = max(odd, even, res, key=len)

        return res

# DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len, start = 1, 0
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start: start + max_len]
# @lc code=end

