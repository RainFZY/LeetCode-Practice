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

        # 从第0个学生开始，dfs搜索这个学生的朋友圈，
        # 搜索到的处于他的朋友圈内的学生visited记为1
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


# 并查集法一
# e.g.
# 初始化father --> [0, 1, 2] # 每个节点的根节点是其本身
# 最后的father --> [1, 1, 2] # 0和1共享一个根节点，2单独一个，因此共两个朋友圈
class Solution:
    def findCircleNum(self, M) -> int:
        # 记录每个学生的根节点
        father = [i for i in range(len(M))]

        # 返回输入节点的根节点
        def find(a):
            if father[a] != a: 
                father[a] = find(father[a])
            return father[a]
        # 合并两个节点，让其中的（任意）一个节点的根节点接到另一个节点的根节点上
        def union(a, b):
            father[find(b)] = find(a)
            return find(b)

        for a in range(len(M)):
            for b in range(a):
                # 互为朋友，合并朋友圈
                if M[a][b] == 1: 
                    union(a, b)
        for i in range(len(M)): 
            find(i)
        
        # 用set()对数组father去重，看有几个独立的朋友圈
        return len(set(father))


# 并查集法二
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        n = len(M)
        # 初始化并查集，令p[i] = i
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(i):
                # 合并所有为 1 的连起来的块，把它们归于一个 parent
                if M[i][j] == 1:
                    self.union(parent, i, j)

        # 返回不同的parent的个数，set用来去重
        return len(set([self.find(parent, i) for i in range(n)]))   

    # 合并
    def union(self, parent, i, j):
        p1 = self.find(parent, i)
        p2 = self.find(parent, j)
        # 如果某两个节点被连通，则让其中的（任意）一个节点的根节点接到另一个节点的根节点上
        # 或者parent[p1] = p2也可以
        parent[p2] = p1

    # 找父节点/领头元素
    def find(self, parent, i):
        root = i
        # 不断地往上找parent
        while parent[root] != root:
            root = parent[root]
        # 路径压缩，这段可以省略
        # while parent[i] != i:
        #     x = i
        #     i = parent[i]
        #     parent[x] = root
        return root

# @lc code=end

