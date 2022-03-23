#
# @lc app=leetcode.cn id=787 lang=python3
#
# [787] K 站中转内最便宜的航班
#

# @lc code=start
# 法一：dp
# dp[t][i]表示从src到i恰好经过t次航班（t条边）的最小价格
# 状态转移方程：dp[t][i] = min(dp[t-1][j] + cost(j, i))
# return: min(dp[t][dst] for t in range(1, k+2))
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k+2条边 = k+1次中转
        dp = [[float("inf")] * n for _ in range(k+2)]
        dp[0][src] = 0 # initialization
        for t in range(1, k+2):
            for [s, v, cost] in flights:
                dp[t][v] = min(dp[t][v], dp[t-1][s] + cost)
        res = min(dp[t][dst] for t in range(1, k+2))
        return -1 if res == float("inf") else res


# 法二：Bellman-Ford
# 根据 Bellman-Ford 算法，经过 k+1 次松弛后，
# dist[dst] 存储的即为源点最多经过 k 个中转站到达 dst 的最小花费
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n # dist[v]表示到达v的最小花费
        dist[src] = 0
        # 对每条边做 k+1 次松弛操作
        for _ in range(k + 1): 
            dist_old = [_ for _ in dist]
            for u, v, w in flights:
                dist[v] = min(dist[v], dist_old[u] + w)

        return dist[dst] if dist[dst] != float('inf') else -1


# @lc code=end

