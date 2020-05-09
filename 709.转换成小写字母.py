#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#

# @lc code=start
# 内置函数
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

# ASCII码，ord()转ASCII码
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for s in str:
            if 65 <= ord(s) <= 90:
                res += chr(ord(s) + 32)
            else:
                res += s
        return res
# @lc code=end

