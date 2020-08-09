#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
# 法一：栈
# 动画见 https://leetcode-cn.com/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode/
# 始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」
# 这样的做法主要是考虑了边界条件的处理，栈里其他元素维护左括号的下标：
# 对于遇到的每个 ‘(’ ，将它的下标放入栈中
# 对于遇到的每个 ‘)’ ，先弹出栈顶元素表示匹配了当前右括号：
# 如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
# 如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」
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

