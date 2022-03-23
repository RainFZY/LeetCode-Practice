#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# 深拷贝(deep copy)即构建一张与原图结构，值均一样的图，
# 但是其中的节点不再是原来图节点的引用。
# 因此，为了深拷贝出整张图，
# 我们需要知道整张图的结构以及对应节点的值。

# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        # return输入node的clone
        def dfs(node):
            if not node:
                return
            if node in lookup:
                return lookup[node]
            # 克隆节点，深拷贝不会克隆它的邻居的列表
            clone = Node(node.val, neighbors=[])
            lookup[node] = clone
            # dfs来填充neighbors列表
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)

# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        def bfs(node):
            if not node:
                return
            clone = Node(node.val, neighbors=[])
            lookup[node] = clone
            queue = []
            queue.append(node)
            while queue:
                temp = queue.pop(0)
                # 原节点的neighbors
                for n in temp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.append(n)
                    # 为克隆节点添加neighbors
                    lookup[temp].neighbors.append(lookup[n])
            return clone
        return bfs(node)
# @lc code=end

