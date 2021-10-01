#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
# 图， 邻接表， 拓扑排序，BFS
# Kahn 算法
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        if n == 0: 
            return [i for i in range(numCourses)]
        # 入度数组，入度越小表示优先级越高
        in_degree = [0 for _ in range(numCourses)]
        # 邻接表
        adj = [set() for _ in range(numCourses)]
        for [child_course, root_course] in prerequisites:
            in_degree[child_course] += 1
            adj[root_course].add(child_course)
        res, queue = [], []
        # 首先遍历一遍，把所有入度为 0 的结点加入队列
        for i in range(numCourses):
            # 入度为0时说明优先级为当前最高，加入队列
            if in_degree[i] == 0:
                queue.append(i)
        while queue:
            root_course = queue.pop(0)
            res.append(root_course)
            for child_course in adj[root_course]:
                in_degree[child_course] -= 1
                if in_degree[child_course] == 0:
                    queue.append(child_course)

        # 对于 Kahn 算法来说，如果最后输出出来的顶点个数，少于图中顶
        # 点个数，图中还有入度不是 0 的顶点，那就说明，图中存在环。
        if len(res) != numCourses:
            return []
        return res
# @lc code=end

