#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
# 法一，二分查找
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 0, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1
        return False


# 法二，牛顿迭代法
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         if num < 2:
#             return True
        
#         x = num // 2
#         while x * x > num:
#             x = (x + num // x) // 2
#         return x * x == num
# @lc code=end

