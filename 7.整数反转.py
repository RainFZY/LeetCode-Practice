#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
# 法一，暴力法
class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            x = int(str_x[::-1])
        else:
            # str_x = str_x[:0:-1]
            str_x = str_x[1:]
            str_x = str_x[::-1]
            x = int(str_x)
            x = -x
        return x if -pow(2, 31) < x < pow(2, 31) - 1 else 0

# 法二
# 重复“弹出” x 的最后一位数字，并将它“推入”到 res 的后面。最后，res 将与 x 相反。
# 要考虑溢出问题
# @lc code=end

