#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
# https://leetcode.cn/problems/is-graph-bipartite/solution/by-shan-gui-tju-c6jx/
#

# @lc code=start
# bipartite grapgh: vertices can be partitioned into two
# sets X, Y such that all edges are crossing between X and Y
# 着色法判断二分图
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.res = True
        n = len(graph)
        visited = [False] * n
        color = [0] * n
        
        def dfs(v):
            if not self.res:
                return
            visited[v] = True
            # 遍历v的所有邻接节点
            for w in graph[v]:
                if not visited[w]:
                    # 如果之前没有经过w，则给w和v不同的颜色
                    color[w] = not color[v]
                    dfs(w)
                else:
                    # 如果邻接两个节点颜色相同，则不是二分图
                    if color[v] == color[w]:
                        self.res = False
                        return
        
        for i in range(n):
            dfs(i)
        return self.res
                    

# @lc code=end

