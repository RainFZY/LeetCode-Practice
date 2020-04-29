#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
# 法一，调用函数
class Solution:
    def hammingWeight(self, n: int) -> int:
        # 把 n转成二进制
        return bin(n).count('1')

# 法二，调用函数
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        count = 0
        for c in n:
            if c == '1':
                count += 1
        return count

# 法三
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            tail = n % 2
            if tail == 1:
                count += 1
            # 右移一位相当于除以2    
            n //= 2
            # n = n >> 1
        return count

# 法四，位运算，runtime更小
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 最后一位跟1与运算
            # x % 2 == 1 --> (x & 1) == 1
            count += n & 1
            n = n >> 1
            # n >>= 1
        return count


# @lc code=end

