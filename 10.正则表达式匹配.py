#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
# s：主串，p：模式串
# 这篇题解非常好：https://leetcode-cn.com/problems/regular-expression-matching/solution/ji-yu-guan-fang-ti-jie-gen-xiang-xi-de-jiang-jie-b/
# 法一，回溯，暴力递归
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        # 如果模式串中有星号，它会出现在第二个位置，即 p[1]，此时可以：
        if len(p) >= 2 and p[1] == '*':
            # 1. 直接忽略模式串中这一部分
            # 2. 若第一字符能匹配，忽略匹配串的第一个字符
            return self.isMatch(s, p[2:]) or \
                first_match and self.isMatch(s[1:], p)
        # 没有星号，则只要一直检查起始字符是否匹配然后跳过即可
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# 法二，DP
# 用 dp(i,j) 表示s[i:] 和 p[j:] 是否能匹配
# 用哈希表 memory[(i, j)]存储二维中间结果
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        def dp(i, j):
            if (i, j) in memory:
                return memory[(i, j)]
            if j == len(p):
                return i == len(s)
            # 这一部分跟法一相同
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p) - 2 and p[j + 1] == '*':
                ans = dp(i, j + 2) or \
                    first_match and dp(i + 1, j)
            else:
                ans = first_match and dp(i + 1, j + 1)
            memory[(i, j)] = ans
            return ans
        return dp(0, 0)
# @lc code=end

