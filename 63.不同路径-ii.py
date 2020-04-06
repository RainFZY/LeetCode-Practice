#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
# 62升级版
# DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 判断第一个格点是否有障碍物
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        # 左边界单独判断
        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
        # 上边界单独判断
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                obstacleGrid[0][j] = obstacleGrid[0][j-1]
            else:
                obstacleGrid[0][j] = 0
        # 去除上、左边界后的其余部分
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
            
        return obstacleGrid[-1][-1]


# 给左面和上面各加一个障碍边，这样不用对边界做判断。
# 最右一列全为0，这样计算左边界时哪怕有-1是+0，不影响结果
# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         array = [1] + [0] * n
#         for i in range(m):
#             for j in range(n):
#                 array[j] = 0 if obstacleGrid[i][j] == 1 else array[j] + array[j - 1]
#         return array[-2]
 
# @lc code=end

