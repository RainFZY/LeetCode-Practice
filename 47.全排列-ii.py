#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
# 可重复数组
# 回溯
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums) # 方便去重
        def backTrack(num, temp):
            if len(temp) == len(nums):
                res.append(temp)
                return
            for i in range(len(num)):
                # 去重
                if i > 0 and num[i] == num[i-1]:
                    continue
                backTrack(num[:i] + num[i+1:], temp + [num[i]])
        backTrack(nums, [])
        return res
# @lc code=end

