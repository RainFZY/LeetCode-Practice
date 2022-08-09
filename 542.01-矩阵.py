#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
# 正向思路，对每个1，用BFS求最近的0的距离，超时
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = mat.copy()
        def bfs(i, j):
            queue = [[i, j]]
            visited = [[0]*n for _ in range(m)]
            distance = 0
            while queue:
                length = len(queue)
                distance += 1
                for _ in range(length):
                    i, j = queue.pop(0)
                    for [x,y] in [[-1,0], [1,0], [0,1], [0,-1]]:
                        temp_x, temp_y = i+x, j+y
                        if 0 <= temp_x < m and 0 <= temp_y < n and \
                            not visited[temp_x][temp_y]:
                            visited[temp_x][temp_y] = 1
                            if mat[temp_x][temp_y] == 0:
                                return distance
                            else:
                                queue.append([temp_x, temp_y])
            return distance
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = bfs(i, j)
        
        return res


# 多源BFS，看题解视频
# https://leetcode.cn/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
# 从矩阵中的所有0开始BFS搜索，每搜一轮就能找到多个1到最近0的距离
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[None for _ in range(n)] for _ in range(m)]
        queue = []  # 存储每个层次上的点
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:  # 将题目转换为 0 到其它点的距离
                    res[i][j] = 0  # 0到自身的距离为零
                    queue.append([i, j])  # 将找到的 0 放入队列
        # BFS
        while queue:
            x, y = queue.pop(0)  # 取出某层上的点，先入先出
            for x_bias, y_bias in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 加四个方向的偏置
                new_x = x + x_bias
                new_y = y + y_bias
                if 0 <= new_x < len(mat) and 0 <= new_y < len(mat[0]) and res[new_x][new_y] == None:  # 判断扩展点有效性
                    res[new_x][new_y] = res[x][y] + 1 # 到最近0的距离为之前点的+1
                    queue.append([new_x, new_y])  # 将新扩展的点加入队列
        return res
# @lc code=end

