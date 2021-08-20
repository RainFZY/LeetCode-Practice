#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
# C的strstr(), Java的indexOf(), python的find()
# 法一，内置函数
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# 法二，滑动窗口
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i: i+n] == needle[:]:
                return i
        return -1

# 法三，双指针
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        left, right = 0, len(needle)
        while right <= len(haystack):
            if haystack[left: right] == needle[:]:
                return left
            left += 1
            right += 1
        return -1



# @lc code=end

