#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
# egg --> 122，add --> 122, True
# foo --> 122, bar --> 123, False
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMapS, hashMapT = {}, {}
        cnt1, cnt2 = 0, 0
        for i in range(len(s)):
            if not hashMapS.get(s[i]):
                hashMapS[s[i]] = cnt1
                cnt1 += 1
            if not hashMapT.get(t[i]):
                hashMapT[t[i]] = cnt2
                cnt2 += 1

        res1, res2 = [], []
        for i in range(len(s)):
            res1.append(hashMapS[s[i]])
            res2.append(hashMapT[t[i]])
        return res1 == res2
# @lc code=end

