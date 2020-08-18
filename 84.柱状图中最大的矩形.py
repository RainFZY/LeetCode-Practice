#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
# 思路:
# 以第i根柱子为最矮柱子所能延伸的最大面积：
# 是以i 为中心，向左找第一个小于 heights[i] 的位置 left_i；
# 向右找第一个小于 heights[i] 的位置 right_i
# 最大面积为 heights[i] * (right_i - left_i -1)

# 法一，双指针，无优化暴力，O(n^2)，超时
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            left, right = i, i
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < n and heights[right] >= heights[i]:
                right += 1
            res = max(res, heights[i] * (right - left - 1))
        return res

# 单调栈，栈内元素保持单调递增，这样遇到一个小于栈顶元素的，就能计算当前位置最大面积
# 如5 6 2时，可以计算 6 位置的最大面积
# 先加进去的可能后面才出来，符合栈，所以用栈
# 动画见https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode/
# 单调栈解析：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/84-by-ikaruga/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # 遇到一个更矮的，那就一直把栈内元素弹出来，直到栈顶比新元素小（重新构成递增序列）
            # 遇到更高的，无法确定，入栈
            while stack and heights[stack[-1]] > heights[i]:
                # 出栈代表可以计算那个位置的最大面积了
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            # 不管高的矮的都添加
            stack.append(i)
        return res

# @lc code=end

