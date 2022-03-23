#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
# 法一，递归+哈希表
# Time Complexity: O(n), Space Complexity: O(n)
hashMap = {0: 0, 1: 1}
class Solution:
    def fib(self, n: int) -> int:
        if n not in hashMap:
            hashMap[n] = self.fib(n-1) + self.fib(n-2)
        return hashMap[n]

# 法二，DP
# Time Complexity: O(n), Space Complexity: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# 法三，迭代
# Time Complexity: O(n), Space Complexity: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        f1, f2, f3 = 0, 1, 1
        for i in range(3, n+1):
            f1 = f2
            f2 = f3
            f3 = f1 + f2
        return f3

# @lc code=end

