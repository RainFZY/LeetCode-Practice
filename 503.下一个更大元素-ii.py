#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
# 单调栈，栈顶最小
# 类似739 每日温度，只不过循环长度得加倍
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n
        for i in range(2 * n):
            # 入栈元素比当前栈顶元素更大，
            # 也就是找到了当前栈顶元素的下一个更大元素，则移除当前栈顶元素
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            stack.append(i % n)
        return res
# @lc code=end

