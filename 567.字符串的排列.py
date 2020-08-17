#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
# 滑动窗口
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        s1 = sorted(s1)
        for i in range(l2 - l1 + 1):
            temp = s2[i: i + l1]
            if sorted(temp) == s1:
                return True
        return False
# @lc code=end

