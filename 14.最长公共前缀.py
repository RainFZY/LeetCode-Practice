#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        # 若以上都没有return，说明第一个字符串就是最长公共前缀
        return strs[0]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or not strs:
            return ""
        s = strs[0]
        for i in range(1, len(strs)):
            # find函数如果包含子字符串则返回开始的索引值，否则返回-1
            while strs[i].find(s) != 0:
                s = s[:-1]
        return s
# @lc code=end

