#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
# 普通方法，超时
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            if self.is_Prime(i):
                count += 1
        return count
    
    def is_Prime(self, n):
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


# 优化，2的倍数提前continue，依然超时
class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            if i == 2:
                count += 1
            if i % 2 == 0:
                continue
            if self.is_Prime(i):
                count += 1
        return count
    
    def is_Prime(self, n):
        for i in range(3, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

# 打表构造
class Solution:
    def countPrimes(self, n: int) -> int:
        ptable = [True for _ in range(n)]
        cnt = 0
        for i in range(2, n):
            if ptable[i]:
                cnt += 1
            m = 2 * i
            while m < n:
                ptable[m] = False
                m += i
        return cnt



# @lc code=end

