#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
from numpy import imag

# DFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        visited = [[0]*n for _ in range(m)]
        def dfs(i, j):
            image[i][j] = color
            visited[i][j] = 1
            for [x,y] in [[-1,0], [0,-1], [1,0], [0,1]]:
                temp_x, temp_y  = i+x, j+y
                if 0 <= temp_x < m and 0 <= temp_y < n and \
                    image[temp_x][temp_y]==target and \
                    not visited[temp_x][temp_y]:
                    dfs(temp_x, temp_y)
            return
        dfs(sr, sc)
        return image

# 删去visited数组
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        def dfs(i, j):
            image[i][j] = color
            for [x,y] in [[-1,0], [0,-1], [1,0], [0,1]]:
                temp_x, temp_y  = i+x, j+y
                if 0 <= temp_x < m and 0 <= temp_y < n and \
                    image[temp_x][temp_y]==target:
                    dfs(temp_x, temp_y)
            return
        if image[sr][sc] != color: 
            dfs(sr, sc)
        return image


# BFS
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        if image[sr][sc] != color: 
            queue = [(sr, sc)]
        else:
            queue = []
        while queue:
            i, j = queue.pop()
            image[i][j] = color
            for [x,y] in [[-1,0], [0,-1], [1,0], [0,1]]:
                temp_x, temp_y  = i+x, j+y
                if 0 <= temp_x < m and 0 <= temp_y < n and \
                    image[temp_x][temp_y]==target:
                    queue.append((temp_x, temp_y))
        return image

# @lc code=end

