#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
# 反转的代码见344：反转字符串
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        # 关建行
        for i in range(0, len(s), 2 * k):
            a[i: i + k] = reversed(a[i: i + k])
        return "".join(a)

# 双指针
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        for i in range(0, len(s), 2 * k):
            left = i
            right = min(left + k - 1, n - 1)
            while left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
        return "".join(s)
# @lc code=end

