#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
# 暴力法，一次循环
# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         res, temp = 1, 1
#         for i in range(1, len(nums)):
#             if nums[i] > nums[i-1]:
#                 temp += 1
#             else:
#                 temp = 1
#             res = max(res, temp)
#         return res

# 法二，滑动窗口
# 左边界设置在每次出现递减的位置
# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         res, left = 1, 0
#         for right in range(1, len(nums)):
#             if nums[right] <= nums[right-1]:
#                 left = right
#             res = max(res, right - left + 1)
#         return res  

# 法三，DP
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            res = max(res, dp[i])
        return res
# @lc code=end

