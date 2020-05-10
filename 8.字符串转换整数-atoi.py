#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        # 去掉空格
        ls = list(str.strip())
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']:
            ls = ls[1:]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))
# @lc code=end

