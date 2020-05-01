#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
# 法一，位运算，通过清零最低位的 1 来实现计数
class Solution:
    def countBits(self, num: int) -> List[int]:
        def countOne(i):
            cnt = 0
            while i != 0:
                # 清零最低位的 1
                i = i & (i - 1)
                cnt += 1
            return cnt
        res = []
        for i in range(num + 1):
            res.append(countOne(i))
        return res

# 法二，DP
# 1的个数：P(x) = P(x // 2) + (x mod 2)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i // 2] + i % 2)
        return res

# 法三，DP
# 1的个数：P(x) = P(x & (x − 1)) + 1
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i & (i - 1)] + 1)
        return res

# 法四，奇偶性
# 奇数：二进制一定比前面那个偶数多一个 1，因为多的就是最低位的 1
# 偶数：1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，
# 除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            if i % 2 == 1:
                res.append(res[i - 1] + 1)
            else:
                res.append(res[i // 2])
        return res
# @lc code=end 

