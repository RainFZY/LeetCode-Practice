#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#

# @lc code=start
# 完全背包问题
# 看示例1，顺序不同的序列被视作不同的组合，因此要考虑顺序
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
        return dp[target]
# @lc code=end

