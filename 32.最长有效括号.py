#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
# 栈，动画见 https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxnum = 0
        # 防止pop时stack为空报错
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                if stack:
                    maxnum = max(maxnum, i - stack[-1])
        return maxnum

# 一维DP，见动画
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxnum = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ")":
                if i - 1 < 0:
                    continue
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                # "))"的情况，比较复杂
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) +2
                maxnum = max(maxnum, dp[i])
        return maxnum
# @lc code=end

