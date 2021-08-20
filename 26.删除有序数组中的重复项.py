#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
# 双指针，类似27
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 0
        n = len(nums)
        for right in range(1, n):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        return left
# @lc code=end

