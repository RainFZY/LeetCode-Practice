#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
# 调用84函数
# 见解法二：https://leetcode-cn.com/problems/maximal-rectangle/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-1-8/
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = matrix
        # 字符串数组转整数数组
        for i in range(len(heights)):
            heights[i] = list(map(int, matrix[i]))
        for i in range(1, len(heights)):
            for j in range(len(heights[0])):
                if heights[i][j] == 1:
                    heights[i][j] += heights[i-1][j]
        res = 0
        for i in range(len(matrix)):
            res = max(res, self.largestRectangleArea(heights[i]))
        return res

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
# @lc code=end

