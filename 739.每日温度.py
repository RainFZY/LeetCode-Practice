#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
# 维护一个存储下标的单调栈，从栈底到栈顶的下标对应的温度列表中的温度依次递减
# 如果一个下标在单调栈里，则表示尚未找到下一次温度更高的下标
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        # 每一个循环必入栈，是否出栈看条件
        for i in range(len(temperatures)):
            temp = temperatures[i]
            # 每次有元素进栈时，会将温度更低的元素全部移除，并更新出栈元素对应的等待天数
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            # 因为要计算的是下标差，所以把下标入栈，而不是温度
            stack.append(i)
        return res
            
# @lc code=end

