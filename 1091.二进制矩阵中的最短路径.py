#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
# 法一，BFS
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = [(0, 0, 2)] # x, y, distance
        n = len(grid)
        directions = [(-1,-1), (1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1)]
        if grid[0][0] or grid[-1][-1]:
            return -1
        elif n <= 2:
            return n
        while queue:
            i, j, step = queue.pop(0)
            # 八连通
            for (dx, dy) in directions:
                x, y = i + dx, j + dy
                # 只有格子为空（0）才能走
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                    if x == n - 1 and y == n - 1:
                        return step
                    queue += [(x, y, step + 1)]
                    # 保证不重复走 
                    grid[x][y] = 1
        return -1

# 法二，A*
# 优先级队列，每次优先走离终点近的点
# 
# @lc code=end

