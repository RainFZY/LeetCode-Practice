#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
# 前缀和 + hashMap
# 前缀和：nums 的第 0 项到 当前项 的和
# prefixSum[x] = nums[0] + nums[1] + … + nums[x]
# nums的某项 = 两个相邻前缀和的差：nums[x] = prefixSum[x] − prefixSum[x−1]
# nums 的 第 i 到 j 项 的和，有：
# nums[i] + … + nums[j] = prefixSum[j] - prefixSum[i - 1]
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int) # 记录前缀和及其出现次数
        hashMap[0] = 1 # 一个数都不取时候的前缀和为1
        cur_sum = 0 # 记录到当前位置的前缀和
        res = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            # 当前前缀和 - 之前某位置前缀和 = k
            if cur_sum - k in hashMap: 
                res += hashMap[cur_sum - k]
            hashMap[cur_sum] += 1
        return res

# dp，裂开了
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = 1 if nums[0] == k else 0
#         for i in range(1, n):
#             if nums[i] == k:
#                 dp[i] = dp[i-1] + 1
#             else:
#                 j = i - 1
#                 temp = nums[i]
#                 while j >= 0:
#                     temp += nums[j]
#                     if temp == k:
#                         dp[i] = dp[i-1] + 1
#                         break
#                     j -= 1
#                 if j == -1:
#                     dp[i] = dp[i-1]
#         return dp[-1]


# @lc code=end

