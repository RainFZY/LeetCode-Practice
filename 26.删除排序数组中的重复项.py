#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
# 双指针法，快指针j迭代，慢指针i计数
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 1
        if length == 0:
            return 0
        for j in range(1,length):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i +=1
        return i
