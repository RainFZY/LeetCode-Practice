#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
# 法一，双指针，先排序
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 先按长度倒序排，再按首字母顺序排
        dictionary.sort(key= lambda x: (-len(x), x))
        for word in dictionary:
            i, j = 0, 0
            count = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    count += 1
                j += 1
            if count == len(word):
                return word
        return ""

# 法二，双指针，不排序
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ''
        for word in dictionary:
            i, j = 0, 0
            count = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                    count += 1
                j += 1
            if count == len(word):
                if len(word) > len(res):
                    res = word
                if len(word) == len(res) and word < res:
                    res = word
        return res
        
# @lc code=end

