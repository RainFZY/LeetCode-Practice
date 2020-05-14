#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        p = sorted(p)
        res = []
        for i in range(len(s) - n + 1):
            temp = s[i: i + n]
            if sorted(temp) == p:
                res.append(i)
        return res
        
# @lc code=end

