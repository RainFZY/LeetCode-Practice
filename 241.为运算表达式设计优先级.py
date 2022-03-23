#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start
# 分治，Divide and Conquer
# 每遇到一个运算符，就分左右两边分别组合
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operators = ['+', '-', '*']
        res = [] # 不是全局变量，函数内变量在递归调用时不会被覆盖
        for i in range(len(expression)):
            if expression[i] in operators:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for j in left:
                    for k in right:
                        if expression[i] == '+':
                            res.append(j+k)
                        elif expression[i] == '-':
                            res.append(j-k)
                        else:
                            res.append(j*k)
        if res == []:
            res.append(int(expression))
        return res

# @lc code=end

