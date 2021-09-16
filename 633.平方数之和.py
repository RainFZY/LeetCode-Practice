#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            temp = left * left + right * right
            if temp == c:
                return True
            elif temp < c:
                left += 1
            else:
                right -= 1
        return False
# @lc code=end

