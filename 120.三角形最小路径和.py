#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
# 法一，DP，自底向上推
# DP方程：f[i, j] = min(f[i + 1, j], f[i + 1, j + 1]) + a[i, j]
# 每个结点处的最小路径 = 它下一层可以动的两个结点的最小路径的较小值 + 结点本身的值
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 新建一个二维数组存储结果，也可以在原数组上直接修改
        dp = triangle
        # 从三角形的倒数第二行开始向上推
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + dp[i][j]
        return dp[0][0]


# 法一，DP，空间优化
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 新建一个一维数组存储结果
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        return res[0]

# 法二，递归，自顶向下
# import functools
# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         # LRU Cache，最近最少使用释放缓存，不然会超时
#         @functools.lru_cache()
#         def recursion(row, column):
#             if row == len(triangle) - 1:
#                 return triangle[row][column]
#             left = recursion(row + 1, column)
#             right = recursion(row + 1, column + 1)
#             return min(left, right) + triangle[row][column]  
        
#         return recursion(0, 0)

# @lc code=end

