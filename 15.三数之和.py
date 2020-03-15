#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# 法一：暴力求解
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         for x in range(len(nums)-2):
#             for y in range(x+1, len(nums)-1):
#                 for z in range(y+1, len(nums)):
#                     if nums[x] + nums[y] + nums[z] == 0:
#                         ans.append([nums[x], nums[y], nums[z]])
#         return ans

# 法二：双指针中间推进
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while j > i and nums[j] == nums[j + 1]: 
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1

        return res

# 法三：哈希表查询

# @lc code=end

