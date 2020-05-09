#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
# 法一，颠倒字符串
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt, flag = 0, 0
        for i in s[::-1]:
            if i == " " and flag == 1:
                return cnt
            if i != " ":
                cnt += 1
                flag = 1
        return cnt

# 法二
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 默认将字符串按照空格分组
        s = s.split()
        return len(s[-1]) if s else 0
# @lc code=end

