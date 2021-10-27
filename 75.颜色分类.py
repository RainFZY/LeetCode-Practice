#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=left
# 三指针，O(n) 最优复杂度
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left指向0的位置，right指向2的位置
        left, right = 0, len(nums)-1
        mid = 0
        while mid <= right:
            cur = nums[mid]
            if cur == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif cur == 2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            else:
                mid += 1
        return nums

# @lc code=right

