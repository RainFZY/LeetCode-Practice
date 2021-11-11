#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
# 库函数
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))

# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                # 因为答案向下保留整数，这里不取mid + 1而是mid
                left = mid + 1
        # 取right是因为可能最后left+1完就比right大了
        return left

# 二分查找，版本二
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right: # 边界条件1
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                # 因为答案向下保留整数，这里不取mid + 1而是mid
                left = mid + 1
        # 取right是因为可能最后left+1完就比right大了
        return right

# 二分查找，版本三
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                # 因为答案向下保留整数，这里不取mid + 1而是mid
                left = mid
        return left

# 法二，牛顿迭代法
# class Solution:
#     def mySqrt(self, x):
#         if x < 2:
#             return x
        
#         x0 = x
#         x1 = (x0 + x / x0) / 2
#         while abs(x0 - x1) >= 1:
#             x0 = x1
#             x1 = (x0 + x / x0) / 2        
            
#         return int(x1)

# @lc code=end

