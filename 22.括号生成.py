#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
# 回溯法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTracking(left = 0, right = 0, s = ""):
            # terminator
            # 终止条件是 if len(s) == 2 * n 也行
            if right == n:
                res.append(s)
                return

            # process（s + "("） + drill down（left + 1）
            # 回溯/递归，if条件判断，对不符合要求的提前剪枝
            # 如果没有两个if就是回溯所有情况
            if left < n:
                backTracking(left + 1, right, s + "(")
            if right < left: # 必须先有左括号再有右括号
                backTracking(left, right + 1, s + ")")

            # reverse state 清理当前层，不用清理
        backTracking()
        return res

# 复习
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backTrack(i, j, temp):
            if i == n and j == n:
                res.append(temp)
                return
            if i < n: # 这行没写出来
                backTrack(i + 1, j, temp + "(")
            if j < i: # 这行没写出来
                backTrack(i, j + 1, temp + ")")
        backTrack(0, 0, "")
        return res


# 生成所有的情况（有效 + 无效）
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]: 
#         res = []
#         def backTracking(i = 0, temp = ""):
#             if i == 2 * n:
#                 res.append(temp)
#                 return
#             backTracking(i + 1, temp + "(")
#             backTracking(i + 1, temp + ")")
#         backTracking()
#         return res

# 复习，生成所有的情况（有效 + 无效）
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         res = []
#         def backTrack(i, temp):
#             if i == 2 * n:
#                 res.append(temp)
#                 return
#             for char in "()":
#                 temp += char
#                 backTrack(i+1, temp)
#                 temp = temp[:-1]
#         backTrack(0, "")
#         return res
# @lc code=end

