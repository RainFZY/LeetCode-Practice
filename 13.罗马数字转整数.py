#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        n = len(s)
        for i in range(n-1):
            # special case
            if hashMap[s[i]] < hashMap[s[i+1]]:
                res -= hashMap[s[i]]
            else:
                res += hashMap[s[i]]

        return res + hashMap[s[-1]]
# @lc code=end

