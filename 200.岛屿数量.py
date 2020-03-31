#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
# Flood Fill算法 + DFS
# DFS探索一片完整的陆地并计数，路过就把它沉为0，避免重复，
class Solution:
    # 方向数组
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = 0
        def dfs(i, j):
            grid[i][j] = "0"
            for x, y in self.directions:
                temp_i = i + x
                temp_j = j + y
                if 0 <= temp_i < m and 0 <= temp_j < n and grid[temp_i][temp_j] == "1":
                    dfs(temp_i, temp_j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res

# @lc code=end

