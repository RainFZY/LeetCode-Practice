#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#

# @lc code=start
# 标准DFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        def dfs(i):
            visited[i] = 1
            for j in rooms[i]:
                if not visited[j]:
                    dfs(j)

        dfs(0)
        for i in range(n):
            if visited[i] == 0:
                return False
        return True

# BFS
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        queue = [0]
        while queue:
            s = queue.pop(0)
            visited[s] = 1
            for v in rooms[s]:
                if not visited[v]:
                    queue.append(v)
        for i in range(n):
            if visited[i] == 0:
                return False
        return True


# @lc code=end

