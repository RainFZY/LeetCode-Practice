#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        # 上下左右边界
        l, r, t, b = 0, n - 1, 0, n - 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num, target = 1, n * n
        while num <= target:
            for i in range(l, r + 1): # left to right
                mat[t][i] = num
                num += 1
            # 更新上边界
            t += 1
            for i in range(t, b + 1): # top to bottom
                mat[i][r] = num
                num += 1
            # 更新右边界
            r -= 1
            for i in range(r, l - 1, -1): # right to left
                mat[b][i] = num
                num += 1
            # 更新下边界
            b -= 1
            for i in range(b, t - 1, -1): # bottom to top
                mat[i][l] = num
                num += 1
            # 更新左边界
            l += 1
        return mat

# @lc code=end

