#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
# 法一，转字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        # if s[0] == "-":
        #     return False
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True 

# 法二，取余得到每一位的数字
# @lc code=end

