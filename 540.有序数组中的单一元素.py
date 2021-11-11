#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
# Binary Search
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            # mid在偶数位，且右边数跟它相等，target从右边跳两格找起
            if mid % 2 == 0 and nums[mid] == nums[mid+1]:
                left = mid + 2
            # mid在奇数位，且左边数跟它相等，target从右边跳一格找起
            elif mid % 2 == 1 and nums[mid] == nums[mid-1]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return ((2*sum(set(nums)))-sum(nums))
# @lc code=end

