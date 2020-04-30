#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
# 位运算
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # n & 1 --> n的最低位
            # 从最低位开始到最高位，不断的将最右边的数移到相应位置
            res += (n & 1) << (31 - i)
            # 右移n更新最低位
            n >>= 1
        return res

        
# @lc code=end

