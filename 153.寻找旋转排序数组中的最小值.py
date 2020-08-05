#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
# 二分查找
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 找到了旋转点，即最小元素
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            else:
                if nums[mid] > nums[right]:
                    # 肯定不在mid，所以可以+1
                    left = mid + 1
                else:
                    # 有可能在mid，所以不+1
                    right = mid
        return nums[left]

# @lc code=end

