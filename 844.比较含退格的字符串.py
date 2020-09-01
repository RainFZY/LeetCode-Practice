#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
# 法一，创建两个栈
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stackS, stackT = [], []
        for i in range(len(S)):
            if S[i] == "#":
                # pop时要注意排除栈为空的情况
                if stackS:
                    stackS.pop()
            else:
                stackS.append(S[i])
        for i in range(len(T)):
            if T[i] == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(T[i])
        return stackS == stackT

# 法二，写一个函数，分别用在两个输入字符串上
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            stack = []
            for i in range(len(s)):
                if s[i] == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(s[i])
            return stack
        return helper(S) == helper(T)


# @lc code=end

