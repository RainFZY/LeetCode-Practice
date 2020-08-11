#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
# 双指针
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        res = []
        j = len(S) - 1
        for i in range(len(S)):
            if S[i].isalpha():
                while not S[j].isalpha():
                    j -= 1
                res.append(S[j])
                j -= 1
            else:
                res.append(S[i])
        return "".join(res)

# 栈
# 两次遍历，一个栈专门存字母，另一个栈存结果
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # letters = [char for char in S if char.isalpha()]
        letters = []
        for char in S:
            if char.isalpha():
                letters.append(char)
        res = []
        for char in S:
            if char.isalpha():
                res.append(letters.pop())
            else:
                res.append(char)
        return "".join(res)
# @lc code=end

