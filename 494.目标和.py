#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start

# minus + plus = target
# minus + plus + (-minus + plus)= target + (-minus + plus)
# 2plus = target + sum
# plus = (target + sum)/2
# --> goal: find some numbers in nums with sum (target + sum)/2
# 转换成0-1背包问题
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = abs(target) # 不加的话输入[100], -200会报错
        new_target = (target + sum(nums))
        if new_target % 2 != 0:
            return 0
        # 接下来套模板
        new_target = new_target // 2
        dp = [0] * (new_target + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(new_target, nums[i]-1, -1):
                dp[j] += dp[j - nums[i]]
        return dp[new_target]
# @lc code=end

