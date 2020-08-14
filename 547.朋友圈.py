#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
# 比较类似 200.岛屿数量，但不一样
# 给定的矩阵可以看成图的邻接矩阵。这样问题可以变成求无向图连通块的个数
# 法一，DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        n = len(M)  
        res = 0
        # 标记每个学生是否已经有朋友圈，0表示无1表示有
        visited = [0] * n
        def dfs(i):
            for j in range(n):
                # i与j联通，先标记为1，再继续搜索j的联通块
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)

        # 对每个编号的学生进行dfs
        for i in range(n):
            # 出现新的联通块
            if visited[i] == 0:
                dfs(i)
                res += 1

        return res


# 法二，BFS
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         if not M:
#             return 0
#         n = len(M)  
#         res = 0
#         visited = set()
#         for i in range(n):
#             if i not in visited:
#                 queue = [i]
#                 while queue:
#                     p = queue.pop(0)
#                     if p not in visited:
#                         visited.add(p)
#                         # 下标，值
#                         for k, num in enumerate(M[p]):
#                             if num == 1 and k not in visited:
#                                 queue += [k]
#                         # queue += [k for k, num in enumerate(M[p]) if num and k not in visited]
#                 res += 1
#         return res
# BFS，不知道哪错了
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         if not M:
#             return 0
#         n = len(M)  
#         res = 0
#         visited = [0] * n
#         for i in range(n):
#             if visited[i] == 0:
#                 queue = [i]
#                 while queue:
#                     p = queue.pop(0)
#                     if visited[p] == 0:
#                         visited[p] == 1
#                         for k, num in enumerate(M[p]):
#                             if num == 1 and visited[k] == 0:
#                                 queue += [k]
#                         # queue += [k for k, num in enumerate(M[p]) if num and k not in visited]
#                 res += 1
#         return res


# 法三，并查集
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         if not M:
#             return 0
#         n = len(M)
#         # 初始化并查集，令p[i] = i
#         p = [i for i in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 # 合并所有为 1 的连起来的块，把它们归于一个 parent
#                 if M[i][j] == 1:
#                     self._union(p, i, j)
#         # 返回不同的parent的个数，set用来去重
#         return len(set([self._parent(p, i) for i in range(n)]))        
    
#     # 合并
#     def _union(self, p, i, j):
#         p1 = self._parent(p, i)
#         p2 = self._parent(p, j)
#         # 如果某两个节点被连通，则让其中的（任意）一个节点的根节点接到另一个节点的根节点上
#         # 或者p[p1] = p2也可以
#         p[p2] = p1

#     # 找父节点/领头元素
#     def _parent(self, p, i):
#         root = i
#         # 不断地往上找parent
#         while p[root] != root:
#             root = p[root]
#         # 路径压缩，这段可以省略
#         while p[i] != i:
#             x = i
#             i = p[i]
#             p[x] = root
#         return root
# @lc code=end

