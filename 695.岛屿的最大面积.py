#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
# DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        m, n = len(grid), len(grid[0])
        # return the area of the current island
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i+1,j) + dfs(i-1,j) + \
                    dfs(i,j-1) + dfs(i, j+1)
            return 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res
# @lc code=end

