#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
# 法一：贪心算法
# 遍历数组，找出每一步时最大的序列和（max_curr）
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         max_curr = nums[0]
#         for i in range(1, len(nums)):
#             max_curr = max(nums[i], max_curr + nums[i])
#             max_sum = max(max_sum, max_curr)
#         return max_sum

# 法二：动态规划，思路基本跟贪心类似
# 对数组进行遍历，对于每一个位置，若它之前的sum为负，说明还不如不要之前只要现在位置的来的大，就抛弃之前的
# sum：当前位置之前的最大连续子序列和
# ans：历史最大连续子序列和
# 如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
# 如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
# 每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
# DP方程：f[i] = max(f[i - 1], 0) + a[i]
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         sum = nums[0]
#         ans = nums[0]
#         for i in range(1, len(nums)):
#             if sum > 0:
#                 sum += nums[i]
#             else:
#                 sum = nums[i]
#             ans = max(ans, sum)
#         return ans

# 法二变式
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = nums[0]
#         for i in range(1, len(nums)):
#             if nums[i - 1] > 0:
#                 nums[i] += nums[i - 1]
#             max_sum = max(max_sum, nums[i])
#         return max_sum

# 法三，把每个位置处的最大值记录一个新的数组中，最后再求max
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        return max(dp)

# @lc code=end

