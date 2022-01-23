#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
# 法一，双指针，排序法寻找中间那段的左右边界
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if sorted(nums) == nums:
            return 0
        n = len(nums)
        sorted_nums = sorted(nums)[:]
        left, right = 0, n-1
        while sorted_nums[left] == nums[left]:
            left += 1
        while sorted_nums[right] == nums[right]:
            right -= 1
                
        return right - left + 1

# 有点难想
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
        # left, right, min_num, max_num = 0, 0, float("inf"), float("-inf")

        # for i, j in enumerate(nums):
        #     if j < max_num:
        #         right = i
        #     max_num = max(max_num, j)

        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] > min_num:
        #         left = i
        #     min_num = min(min_num, nums[i])
        # return 0 if left == right else right - left + 1



# @lc code=end

