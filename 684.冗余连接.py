#
# @lc app=leetcode.cn id=684 lang=python3
#
# [684] 冗余连接
#

# @lc code=start
# 并查集
# https://leetcode.cn/problems/redundant-connection/solution/rong-yu-lian-jie-by-leetcode-solution-pks2/
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # 先将它们的父节点设为自己，[0,1,2,...,n]
        parent = list(range(n + 1))

        # 如果当前的x不是其父节点，就找到当前x的父节点的
        # 根节点(find(parents[x])) 并将这个值赋值给x的父节点
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        
        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            # 如果两个顶点属于不同的连通分量，合并这两个顶点的连通分量
            if find(node1) != find(node2):
                union(node1, node2)
            # 如果两个顶点属于相同的连通分量，则说明在遍历到当前的边之前，
            # 这两个顶点之间已经连通，因此当前的边导致环出现，为附加的边，
            # 将当前的边作为答案返回
            else:
                return [node1, node2]
        
        return []
# @lc code=end

