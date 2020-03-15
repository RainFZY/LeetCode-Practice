#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start

# 法一：排序法
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# 法二：哈希表法，统计每个字符的频次
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        for char in s:
            # value代表个数，若不存在就初始化为0
            hashMapS[char] = hashMapS.get(char, 0) + 1
        for char in t:
            hashMapT[char] = hashMapT.get(char, 0) + 1
        return hashMapS == hashMapT

# @lc code=end

