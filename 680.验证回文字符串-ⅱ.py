#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
# 双指针
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # 去掉右边的，去掉左边的
                case1, case2 = s[left: right], s[left + 1: right + 1]
                # 最多删除一个字符，必须return
                return case1[::-1] == case1 or case2[::-1] == case2
            left += 1
            right -= 1
        return True
# @lc code=end

