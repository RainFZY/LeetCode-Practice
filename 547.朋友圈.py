#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
# 同 200.岛屿数量
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 方向数组
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        m = len(M)
        if m == 0:
            return 0
        n = len(M[0])
        res = 0
        def dfs(i, j):
            M[i][j] = 0
            for [x, y] in directions:
                temp_i = i + x
                temp_j = j + y
                if 0 <= temp_i < m and 0 <= temp_j < n and \
                    M[temp_i][temp_j] == 1:
                    dfs(temp_i, temp_j)
        
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    # 把包含这块的整片陆地给沉了
                    dfs(i, j)
                    res += 1

        return res
        
# @lc code=end

