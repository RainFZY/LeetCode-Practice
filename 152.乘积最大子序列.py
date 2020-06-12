#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

# @lc code=start
# DP，记录最小值与最大值
# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         min_ = max_ = res = nums[0]
#         for i in range(1, len(nums)):
#             # 这步很难想到，负数的话交换最大最小
#             if nums[i] < 0:
#                 min_, max_ = max_, min_
#             max_ = max(max_ * nums[i], nums[i])
#             min_ = min(min_ * nums[i], nums[i])
#             res = max(res, max_)
#         return res

# DP，更加老实的方法
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = max_ = res = nums[0]
        for i in range(1, len(nums)):
            max_, min_ = \
            max(max_ * nums[i], nums[i], min_ * nums[i]), \
            min(max_ * nums[i], nums[i], min_ * nums[i])
            res = max(res, max_)
        return res
# @lc code=end

