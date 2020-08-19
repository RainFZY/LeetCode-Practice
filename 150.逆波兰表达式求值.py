#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
# 栈
# 遇到数字压入栈, 遇到操作符, 弹出栈顶两个元素操作
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        plus = lambda a, b: b + a
        sub = lambda a, b: b - a
        mul = lambda a, b: b * a
        # 整数除法只保留整数部分, //是向下取整，在负数时错误
        div = lambda a, b: int(b / a)
        opt = {
            "+": plus,
            "-": sub,
            "*": mul,
            "/": div
        }
        for t in tokens:
            # 是字符，就加入最近两个数运算后的结果（最近相关性）
            if t in opt:
                stack.append(opt[t](stack.pop(), stack.pop()))
            # 是数字，就加入数字
            else:
                stack.append(int(t))
        return stack.pop()
# @lc code=end

