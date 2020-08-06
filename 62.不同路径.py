#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# DP动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个m * n的二维数组
        # 必须得初始化为1，代表到某个点有1种走法
        array = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                array[i][j] = array[i - 1][j] + array[i][j - 1]
        return array[-1][-1]


# DP动态规划优化版：
# 第(i,j)的路径和是由上面的和左面的相加得到
# 设置一个一维的数组来保存每一行的节点的路径和
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        array = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # 新的一行j位置处的路径数 = 上边位置路径数（此时还未更新，上下相等） + 左边位置路径数
                array[j] = array[j] + array[j - 1]
        return array[-1]
# @lc code=end

