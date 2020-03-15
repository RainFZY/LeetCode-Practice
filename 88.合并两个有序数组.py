#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start

# 法一
# 这种方法没有利用两个数组本身已经有序这一点
# 时间复杂度较差，为O((n+m)log(n+m))
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[:] = nums1[:m] + nums2
#         nums1[:] = sorted(nums1)
#         # nums1.sort()
 

# 法二：双指针
# O(m+n)时间复杂度
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        nums1[:] = [] # 这里一定要加:，保留数组的长度（内存空间）
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]

        
# @lc code=end

