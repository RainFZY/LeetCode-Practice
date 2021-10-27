#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            cnt += self.extend(s, i, i)
            cnt += self.extend(s, i, i+1)
        return cnt

    def extend(self, s, i, j):
        cnt = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            cnt += 1
        return cnt

# @lc code=end

