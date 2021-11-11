#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
# Binary Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return right
        # 搜索左边界：第一个大于等于 target的下标
        leftBorder = binarySearch(target) 
        # 搜索右边界：第一个大于等于 target+1的下标， 减1则得到rightBorder
        rightBorder = binarySearch(target + 1) - 1
        # 搜索不到
        if leftBorder == len(nums) or nums[leftBorder] != target:
            return [-1, -1]
        return [leftBorder, rightBorder]




# 寻找左侧边界的二分查找 + 寻找右侧边界的二分查找
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return [-1, -1]
#         # 找开始位置（寻找左侧边界的二分查找）
#         # 搜索区间为 [left, right]，左右都闭
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             # 查找到目标值，不急着返回，收缩右边界，看左边是否还有重复元素
#             if nums[mid] == target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         # 检查出界情况
#         if left >= len(nums) or nums[left] != target:
#             start = -1
#         else:
#             start = left

#         # 找结束位置（寻找右侧边界的二分查找）
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             # 查找到目标值，不急着返回，收缩左边界，看右边是否还有重复元素
#             if nums[mid] == target:
#                 left = mid + 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         # 检查出界情况
#         if right >= len(nums) or nums[right] != target:
#             end = -1
#         else:
#             end = right

#         return [start, end]
# @lc code=end

