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

# BFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        res = 0
        def bfs(i, j):
            queue = [(i, j)]
            area = 1
            grid[i][j] = 0 # 保证第一次进来时第一个点变成0
            while queue:
                x, y = queue.pop(0)
                for [dx, dy] in directions:
                    temp_x, temp_y = x+dx, y+dy
                    if 0 <= temp_x < m and 0 <= temp_y < n and \
                        grid[temp_x][temp_y] == 1:
                        grid[temp_x][temp_y] = 0
                        area += 1
                        queue.append((temp_x, temp_y))
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))
        return res
# @lc code=end

