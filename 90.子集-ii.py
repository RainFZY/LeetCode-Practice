#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
# 重复数组
# 回溯
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums) # 别漏了这一步
        def backTrack(start, temp):
            if len(temp) > len(nums):
                return
            res.append(temp[:])
            for i in range(start, len(nums)):
                # 关键行，剔除重复解，同 40 组合总和Ⅱ
                if i > start and nums[i] == nums[i-1]: 
                    continue
                temp.append(nums[i])
                backTrack(i+1, temp)
                temp.pop()
        backTrack(0, [])
        return res
# @lc code=end

