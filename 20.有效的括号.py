#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
# 思路：栈+哈希表
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['?'] # 创建栈，由于空栈的pop会报错，事先加入一个元素
        map = {"(":")", "[":"]", "{":"}", "?":"?"}
        for char in s:
            # 判断是否是左边的括号，in map是查询字典的key
            if char in map: 
                stack.append(char) # 入栈
            # 是右边的括号的情况：
            else:
                if char != map[stack.pop()]: # 出栈操作，出key，再到map里面对应value
                    return False
        return len(stack) == 1
 
# @lc code=end

