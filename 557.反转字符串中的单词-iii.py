#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
# 法一，两次反转
# 发现，输出的反转过来就是"contest LeetCode take Let's"，根据这个思路来做
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        s = " ".join(s)
        return s[::-1]
        
# 栈，利用栈的先入后出性质反转单词
class Solution:
    def reverseWords(self, s: str) -> str:
        stack, res = [], ""
        # 在原字符串末尾补充一个空格，让每一小节都变成“单词+空格”
        s = s + " "
        for i in s:
            stack.append(i)
            # 遇见空格就是判断出栈的前提条件
            if i == " ":
                while stack:
                    res += stack.pop()
        return res[1:]
# @lc code=end

