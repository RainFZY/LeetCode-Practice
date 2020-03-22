#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
# 二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid_index = left + (right - left) // 2
            mid_num = matrix[mid_index // n][mid_index % n]
            if mid_num == target:
                return True
            elif mid_num > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return False
# @lc code=end

