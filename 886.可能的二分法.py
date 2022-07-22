#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start



# 同[785] 判断二分图，区别是这道题要先写个函数建邻接矩阵
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        visited = [False] * (n+1)
        color = [0] * (n+1)
        self.res = True
        graph = self.buildGraph(n, dislikes)

        def dfs(v):
            if not self.res:
                return
            visited[v] = True
            for w in graph[v]:
                if not visited[w]:
                    color[w] = not color[v]
                    dfs(w)
                else:
                    if color[v] == color[w]:
                        self.res = False
                        return
        for i in range(1, n+1):
            dfs(i)
        return self.res
    
    # 将dislikes转成邻接矩阵
    def buildGraph(self, n, dislikes):
        graph = [[] for i in range(n+1)]
        for [i,j] in dislikes:
             graph[i].append(j)
             graph[j].append(i)
        return graph
# @lc code=end

