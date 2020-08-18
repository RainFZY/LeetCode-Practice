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
        right = len(S) - 1
        for left in range(len(S)):
            # 左是字母，就寻找右边第一个是字母的添加到res
            if S[left].isalpha():
                while not S[right].isalpha():
                    right -= 1
                res.append(S[right])
                right -= 1
            # 左不是字母，直接添加到res
            else:
                res.append(S[left])
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

