#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start

# Dijkstra 最短路径算法
# n: num of nodes, k: source node
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 邻接矩阵 Adjacency Matrix
        adj = [[float('inf')] * n for _ in range(n)]
        for [u, v, w] in times:
            adj[u-1][v-1] = w
        
        # dist数组，记录每个node到k到最短距离
        dist = [float('inf')] * n
        dist[k-1] = 0

        discovered = [False] * n
        # 每个循环更新一个未标记的最近的点，共n个
        for _ in range(n):
            # 找到未标记的最近的点，记为x
            x = -1
            for y, discovered_flag in enumerate(discovered):
                if discovered_flag == False \
                    and (x == -1 or dist[y] < dist[x]):
                    x = y
            discovered[x] = True
            # 更新dist
            for y, time in enumerate(adj[x]):
                dist[y] = min(dist[y], dist[x] + time)
        
        if max(dist) < float('inf'):
            res = max(dist)
        else:
            res = -1

        return res





# @lc code=end

