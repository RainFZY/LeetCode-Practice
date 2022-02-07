#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
# 栈，感觉很难
class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # [(str, int)] 记录左括号之前的字符串和左括号外的上一个数字
        res = "" # 实时记录当前可以提取出来的字符串
        num = 0
        for char in s:
            # 遇到数字
            if "0" <= char <= "9":
                num = num * 10 + int(char)
            # 遇到左括号，让左括号外的上一个数字和左括号之前的字符串入栈，并清零
            elif char == "[":
                stack.append([num, res])
                num, res = 0, ""
            # 遇到右括号，让最近的一组出栈并更新res
            elif char == "]":
                last_num, last_res = stack.pop()
                res = last_res + last_num * res # e.g. res = a + 2*c = acc
            # 遇到字母
            else:
                res += char
        return res

# @lc code=end

