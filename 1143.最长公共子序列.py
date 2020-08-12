#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
# 类似字符串编辑距离问题，转化成二维数组递推问题，类似于62，不同路径问题，左上到右下不断更新矩阵
# DP，自底向上
# 图看这篇题解：https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)
        # 专门让索引为 0 的行和列表示空串，防止边界溢出，因此是n + 1和m + 1
        # dp[0][..] 和 dp[..][0] 都应该初始化为 0，这就是 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 由于dp矩阵相比原字符串多了一行一列0，这里要-1
                # 若存在相同的字符，就等于在两边各去掉这个字符后的最长公共子序列+1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


# 法二，递归 + 哈希表二维存储，自顶向下
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hashMap = {}
        def recursion(i, j):
            if hashMap.get((i, j)):
                return hashMap[(i, j)]
            # terminatior
            # -1 是由 i = 0 或 j = 0时drill down后 i-1 或 j-1得到的
            if i == -1 or j == -1:
                return 0
            # drill down
            if text1[i] == text2[j]:
                hashMap[(i, j)] = recursion(i-1, j-1) + 1
            else:
                hashMap[(i, j)] = max(recursion(i-1, j), recursion(i, j-1))
            return hashMap[(i, j)]
        return recursion(len(text1)-1, len(text2)-1)


# 法三，递归 + lru_cache
import functools
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(None)
        def recursion(i, j):
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                return recursion(i - 1, j - 1) + 1
            else:
                return max(recursion(i - 1, j), recursion(i, j - 1))
        return recursion(len(text1) - 1, len(text2) - 1)
            
# @lc code=end

