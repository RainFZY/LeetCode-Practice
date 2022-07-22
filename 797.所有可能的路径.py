#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start

# 输入的图是无环的，就不需要visited数组
# DFS，回溯
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res, temp = [], [0]
        def dfs(u):
            if u == len(graph) - 1:
                res.append(temp)
                return
            for v in graph[u]:
                temp.append(v)
                dfs(v)
                temp.pop()

        dfs(0)
        return res

# @lc code=end

