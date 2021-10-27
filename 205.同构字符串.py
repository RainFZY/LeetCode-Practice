#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start

# 法一
# egg --> 122
# bar --> 123
# paper --> 12134
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapA, hashMapB = {}, {}
        for i in range(len(s)):
            hashMapA[s[i]] = hashMapA.get(s[i], i)
            hashMapB[t[i]] = hashMapB.get(t[i], i)
            # 提前剪枝
            if hashMapA[s[i]] != hashMapB[t[i]]:
                return False
        return True

# @lc code=end

