#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
# 回溯法，类似22
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        temp = []
        m = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backTracking(i, digits):
            # terminator
            if i == len(digits):
                # 实现把"temp"加入ans
                ans.append("".join(temp)) 
                return
            for char in m[digits[i]]:
                # process
                temp.append(char)
                # drill down
                backTracking(i+1, digits)
                # reverse state
                temp.pop()
        backTracking(0, digits)
        return ans


# 变式，process && drill down 二合一
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        temp = []
        m = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def backTracking(i, digits, temp):
            # terminator
            if i == len(digits):
                # 实现把"temp"加入ans
                # 把temp数组转字符串
                ans.append("".join(temp)) 
                return
            for char in m[digits[i]]:
                # process && drill down 
                backTracking(i+1, digits, temp + [char])
        backTracking(0, digits, [])
        return ans

# @lc code=end

