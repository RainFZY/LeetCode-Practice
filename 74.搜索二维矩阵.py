#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
# 法一，二维矩阵二分查找
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


# 法二，把二维矩阵展成一维数组，二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        for i in range(m):
            array += matrix[i]
        left, right = 0, m * n -1
        while left <= right:
            mid = left + (right - left) // 2
            if target == array[mid]:
                return True
            elif target < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
# @lc code=end

