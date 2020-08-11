#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            # 字母
            if char.isalpha():
                res += char.lower()
            # 数字
            if char.isdigit():
                res += char
        # if ''.join(reversed(res)) == res
        return True if res[::-1] == res else False

# 双指针
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # 跳过其他非字母/数字字符，排除干扰
            # isalnum: num + alpha
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
# @lc code=end

