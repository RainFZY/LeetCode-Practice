#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
# 枚举三个数，循环固定一个数 + 双指针 优化暴力枚举
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            start, end = i + 1, n - 1
            while start < end:
                temp = nums[i] + nums[start] + nums[end]
                if abs(target - temp) < abs(target - res):
                    res = temp
                if target > temp:
                    start += 1
                elif target < temp:
                    end -= 1
                else:
                    return res
        return res
# @lc code=end

