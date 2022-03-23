#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
# DFS + Flood Fill算法
# DFS探索一片完整的陆地并计数，路过就把它沉为0，避免重复，
# 动画见：
# https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 方向数组
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        res = 0
        def dfs(i, j):
            # 沉岛
            grid[i][j] = "0"
            for [x, y] in directions:
                temp_i = i + x
                temp_j = j + y
                if 0 <= temp_i < m and 0 <= temp_j < n and \
                    grid[temp_i][temp_j] == "1":
                    dfs(temp_i, temp_j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 把包含这块的整片陆地给沉了
                    dfs(i, j)
                    res += 1

        return res

# BFS，非递归标准写法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        m, n = len(grid), len(grid[0])
        cnt = 0
        def bfs(i, j):
            grid[i][j] = "0" # 相当于visited数组的作用，标记来过
            queue = []
            queue.append((i, j))
            while queue:
                (i, j) = queue.pop(0) # pop(0)
                for (x, y) in directions:
                    temp_x, temp_y = i+x, j+y
                    if 0 <= temp_x < m and 0 <= temp_y < n \
                        and grid[temp_x][temp_y] == "1":
                        grid[temp_x][temp_y] = "0"
                        queue.append((temp_x, temp_y))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(i, j)
        return cnt

# BFS，递归写法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        m, n = len(grid), len(grid[0])
        cnt = 0
        def bfs(i, j):
            grid[i][j] = "0"
            queue = []
            queue.append((i, j))
            while queue:
                (i, j) = queue.pop(0)
                for (x, y) in directions:
                    temp_x, temp_y = i+x, j+y
                    if 0 <= temp_x < m and 0 <= temp_y < n \
                        and grid[temp_x][temp_y] == "1":
                        bfs(temp_x, temp_y) # 递归
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(i, j)
        return cnt



# 复习，dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        row, col = len(grid), len(grid[0])
        cnt = 0
        def dfs(i, j):
            grid[i][j] = "0"
            for [x, y] in directions:
                temp_x, temp_y = i + x, j + y
                if 0 <= temp_x < row and 0 <= temp_y < col \
                    and grid[temp_x][temp_y] == "1":
                    dfs(temp_x, temp_y)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt







# @lc code=end

