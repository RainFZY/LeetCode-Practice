#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
# binary search
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/shuang-zhi-zhen-by-powcai/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2,nums1)
        k = (n1 + n2 + 1)//2 # 左半边总个数
        # binary search查找边界值(确定m1, m2)
        left, right = 0, n1
        while left < right:
            m1 = left +(right - left)//2 # num1中的左半边总个数
            m2 = k - m1 # num2中的左半边总个数
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1 

        # c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf") )
        # if (n1 + n2) % 2 == 1:
        #     return c1
        # c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
        # return (c1 + c2) / 2
        # 边界条件处理：易读版
        if m1 == 0:
            mid1 = nums2[m2 - 1]
        elif m2 == 0:
            mid1 = nums1[m1 - 1]
        else:
            mid1 = max(nums1[m1 - 1], nums2[m2 - 1])
        if (n1 + n2) & 1:
            return mid1

        if m1 == n1:
            mid2 = nums2[m2]
        elif m2 == n2:
            mid2 = nums1[m1]
        else:
            mid2 = min(nums1[m1], nums2[m2])
        return (mid1 + mid2) / 2

# quick sort
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        res = sorted(nums1 + nums2)
        return res[(n1+n2)//2] if (n1+n2)%2 else (res[(n1+n2)//2] + res[(n1+n2)//2-1]) / 2 



# @lc code=end

