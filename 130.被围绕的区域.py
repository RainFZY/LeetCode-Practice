#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
# 从边界出发，先DFS把边界上和 O 连通点找到, 把这些变成 B
# 然后遍历整个 board 把 O 变成 X, 把 B 变成 O
# 法一，DFS
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if not board or not board[0]:
#             return
#         row = len(board)
#         col = len(board[0])

#         def dfs(i, j):
#             board[i][j] = "B"
#             for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 temp_i = i + x
#                 temp_j = j + y
#                 if 1 <= temp_i < row and 1 <= temp_j < col and \
#                     board[temp_i][temp_j] == "O":
#                     dfs(temp_i, temp_j)

#         for j in range(col):
#             # 第一行
#             if board[0][j] == "O":
#                 dfs(0, j)
#             # 最后一行
#             if board[row - 1][j] == "O":
#                 dfs(row - 1, j)
        
#         for i in range(row):
#             # 第一列
#             if board[i][0] == "O":
#                 dfs(i, 0)
#             # 最后一列
#             if board[i][col-1] == "O":
#                 dfs(i, col - 1)
        
#         for i in range(row):
#             for j in range(col):
#                 # O变成 X
#                 if board[i][j] == "O":
#                     board[i][j] = "X"
#                 # B 变成 O
#                 if board[i][j] == "B":
#                     board[i][j] = "O"

# BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            # queue = deque()
            queue = []
            # queue.appendleft((i, j))
            queue.insert(0, (i, j))
            while queue:
                (i, j) = queue.pop()
                if 0 <= i < row and 0 <= j < col and board[i][j] == "O":
                    board[i][j] = "B"
                    for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        # queue.appendleft((i + x, j + y))
                        queue.insert(0, (i + x, j + y))

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                bfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                bfs(row - 1, j)
        
        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                bfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                bfs(i, col - 1)
        
        for i in range(row):
            for j in range(col):
                # O变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"

# 并查集
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         f = {}
#         def find(x):
#             f.setdefault(x, x)
#             if f[x] != x:
#                 f[x] = find(f[x])
#             return f[x]
#         def union(x, y):
#             f[find(y)] = find(x)

            
            
#         if not board or not board[0]:
#             return
#         row = len(board)
#         col = len(board[0])
#         dummy = row * col
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j] == "O":
#                     if i == 0 or i == row - 1 or j == 0 or j == col - 1:
#                         union(i * col + j, dummy)
#                     else:
#                         for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                             if board[i + x][j + y] == "O":
#                                 union(i * col + j, (i + x) * col + (j + y))
#         for i in range(row):
#             for j in range(col):
#                 if find(dummy) == find(i * col + j):
#                     board[i][j] = "O"
#                 else:
#                     board[i][j] = "X"


# @lc code=end

