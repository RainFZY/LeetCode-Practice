#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashMap = {}
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        for char in s:
            if hashMap[char] == 1:
                return s.index(char)
        return -1
        
            
# @lc code=end

