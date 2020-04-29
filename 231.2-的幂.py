#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
# 一个数若为 2 的幂次方，则有且只有一个 1
# 法一，位运算清零最低位 1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 清零 n 最低位的 1
        # n = n & (n - 1) 
        return n != 0 and (n & (n - 1)) == 0

# 法二，傻办法统计 1 的个数，同 191
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        n = bin(n)
        count = 0
        for c in n:
            if c == '1':
                count += 1
        return count == 1
# @lc code=end

