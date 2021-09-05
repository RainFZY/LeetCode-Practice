#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量，似于200.岛屿数量
#

# @lc code=start
# 法一，DFS
# 虽然输入是二维数组，但是可以直接在一维上进行遍历
# 因为比如(1, 3)和(3, 1)表达的都是city 1和3的关系
# 因此就不需要direction数组了
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 以 i 为起点开始深度优先搜索
        def dfs(i):
            # 一维数组进行标记
            visited[i] = 1
            # 继续搜索与 i 相连的城市
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        # 城市数量
        n = len(isConnected)
        # visited 用以标记城市是否被访问
        visited = [0] * n
        # 用以存储省份的数量
        count = 0
        # 遍历城市进行搜索
        for i in range(n):
            # 城市未被访问时，开始搜索
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count

# 法二，BFS，非递归写法
# BFS与DFS一样，都是一次性遍历完连接的一片区域，然后计数+1
# 区别在于比如 4 <- 2 <- 1 -> 3的情况，BFS是1遍历到2然后到3，DFS是1到2到4，再到3
import collections
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        count = 0
        queue = collections.deque()

        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                count += 1
                queue.append(i)
            
            while queue:
                # 出队开始搜索
                u = queue.popleft()
                # 搜索与 u 相连且未被访问的城市
                for v in range(n):
                    if isConnected[u][v] == 1 and not visited[v]:
                        visited[v] = 1
                        queue.append(v)
        
        return count

# 法三，并查集
class UnionFind:
    def __init__(self):
        # 记录每个节点的父节点
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0
    # 查找祖先的方法是：如果节点的父节点不为空，那就不断迭代
    def find(self,x):
        root = x
        
        while self.father[root] != None:
            root = self.father[root]
        
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        
        return root
    # 如果发现两个节点是连通的，那么就要把他们合并，也就是他们的祖先是相同的
    def merge(self,x,y):
        root_x,root_y = self.find(x),self.find(y)
        
        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1
    
    # 添加新节点
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(M)):
            uf.add(i)
            for j in range(i):
                if M[i][j]:
                    uf.merge(i,j)
        
        return uf.num_of_sets

# 复习，DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        cnt = 0
        visited = [0] * n
        def dfs(i):
            visited[i] = 1
            for j in range(n):
                if not visited[j] and M[i][j] == 1:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                cnt += 1
                dfs(i)
        return cnt

# 复习，BFS，递归写法
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        n = len(isConnected)
        visited = [0] * n
        def bfs(i):
            queue = []
            queue.append(i)
            while queue:
                i = queue.pop(0)
                visited[i] = 1
                for j in range(n):
                    if isConnected[i][j] == 1 and not visited[j]:
                        queue.append(j)
        for i in range(n):
            if not visited[i]:
                cnt += 1
                bfs(i)
        return cnt

# @lc code=end

