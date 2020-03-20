#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
# 法一，暴力法，O(n)，超时
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             n = -n
#             x = 1/x
#         res = 1
#         for i in range(n):
#             res *= x
#         return res

# 法二，递归
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        def recursion(x, n):
            if n == 0:
                return 1
            # 向下取整
            half = recursion(x, n//2)
            if n % 2 == 1:
                return half * half * x
            else:
                return half * half
        return recursion(x,n)

# 法三，递归变式，不知道为什么错了
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             n = -n
#             x = 1/x
#         res = 1
#         def recursion(x, n):
#             if n == 0:
#                 return 
#             # 向下取整
#             recursion(x, n//2)
#             if n % 2 == 1:
#                 res = res * res * x
#             else:
#                 res = res * res

#         recursion(x,n)
#         return res
# @lc code=end

