#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
# 法一，非原地
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                # 找关系
                # 矩阵中第i行的第j个元素，旋转后出现在倒数第i列的第j个位置
                new_matrix[i][j] = matrix[n-j-1][i]
        matrix[:] = new_matrix
        return matrix

# 法二，旋转可以用 水平翻转 + 主对角线翻转 实现
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 水平翻转
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix

# 法三，原地旋转
# e.g. 示例2中，5, 11, 16, 15互相换位置
# 1, 10, 12, 13互相换位置
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 按逆时针顺序写的
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]



# @lc code=end

