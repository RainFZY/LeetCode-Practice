#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
# 将非零位排序，之后补零
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0 # 记非零个数
        for i in range(n):
            if(nums[i] != 0):
                nums[count] = nums[i]
                count += 1
        
        for i in range(count, n):
            nums[i] = 0

# @lc code=end

