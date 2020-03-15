#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start

# 1: 1
# 2: 2
# 3: f(1) + f(2)
# 4: f(2) + f(3) 
# n: f(n-2) + f(n-1) 最后一次的情况是跨一步或者跨两步(找最近的重复子问题)
# 求斐波那契数列的第n项

# 法一：迭代
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         f1, f2, f3 = 1, 2, 3
#         if n <= 2:
#             return n
#         for i in range(3, n):
#             f1 = f2
#             f2 = f3
#             f3 = f1 + f2
#         return f3

# 法二：递归 + 哈希表存储
# 直接用递归的话计算超时
harshMap = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # 如果之前已经计算过（存储在哈希表中），就直接调用，避免重复计算
        if harshMap.get(n):
            return harshMap.get(n)
        harshMap[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# @lc code=end

