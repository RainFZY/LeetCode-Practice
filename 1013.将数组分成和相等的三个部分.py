#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        s /= 3
        cur = 0
        for i in range(len(A)):
            cur += A[i]
            if cur == s:
                break
        if cur != s:
            return False
        for j in range(i+1,len(A)-1):
            cur += A[j]
            if cur == s * 2:
                return True
        return False
        
# @lc code=end

