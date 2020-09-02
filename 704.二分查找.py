#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
# nums中元素无重复
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 搜索区间为 [left, right]，左右都闭
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# 若数组中可能有重复元素（有或没有都适用）
# 寻找左侧边界的二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 搜索区间为 [left, right]，左右都闭
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 查找到目标值，不急着返回，收缩右边界，看左边是否还有重复元素
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # 检查出界情况
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
        
# @lc code=end

