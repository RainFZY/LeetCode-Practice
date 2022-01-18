#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
# 法一，bin转二进制字符串
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        if len(x) < len(y):
            x = '0' * (len(y) - len(x)) + x
        else:
            y = '0' * (len(x) - len(y)) + y
        cnt = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
        return cnt

# 法二，位运算
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y # 按位异或（相同为0不同为1）
        res = str(bin(z)).count("1")
        # # 或者不用bin的方法
        # res = 0
        # while z:
        #     if z & 1:
        #         res += 1
        #     z >>= 1
        return res




# @lc code=end

