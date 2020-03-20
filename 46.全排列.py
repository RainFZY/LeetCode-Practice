#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
# 回溯，实在难懂
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backTracking(nums, temp):
            if len(temp) == n:
                res.append(temp)
                return 
            for i in range(len(nums)):
                # 若nums[:0]返回的是[]
                backTracking(nums[:i] + nums[i+1:], temp + [nums[i]])
        backTracking(nums,[])
        return res
# @lc code=end

