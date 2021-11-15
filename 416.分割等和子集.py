#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
# 非完全0-1背包问题
# dp，一维table
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]

# dp，二维table
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0] <= target:
            dp[0][nums[0]] = True
        # 再填表格第 1 列， target若为0则所有都可以
        for i in range(len(nums)):
            dp[i][0] = True
        for i in range(1, len(nums)):
            for j in range(target+1):
                # 直接从上一行先把结果抄下来，然后再修正
                dp[i][j] = dp[i-1][j]
                if nums[i] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]
# @lc code=end

