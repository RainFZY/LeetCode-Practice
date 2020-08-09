#
# @lc app=leetcode.cn id=866 lang=python3
#
# [866] 回文素数
#

# @lc code=start
# 遗憾超时，懒得优化
class Solution:
    def primePalindrome(self, N: int) -> int:
        # 素数
        def is_Prime(n):
            if n == 1:
                return False
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        # 回文数
        def isPalindrome(x):
            s = str(x)
            n = len(s)
            for i in range(n // 2):
                if s[i] != s[n - 1 - i]:
                    return False
            return True
        
        for i in range(N, 10 ** 8):
            if is_Prime(i) and isPalindrome(i):
                return i




        
# @lc code=end

