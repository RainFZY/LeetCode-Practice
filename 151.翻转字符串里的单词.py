#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        # s = reversed(s)
        s.reverse()
        return " ".join(s)
# @lc code=end

