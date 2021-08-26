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

# 复习
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        m = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # i用来计 遍历到了digits的第几个字母
        def backTrack(i, temp):
            if len(temp) == len(digits): # if i == len(digits): 也行
                ans.append(temp)
                return
            for char in m[digits[i]]:
                temp += char
                backTrack(i+1, temp)
                temp = temp[:-1] # 字符串删除最后一个字符
        backTrack(0, "")
        return ans

# @lc code=end

