#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
# 法一，迭代
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for i in nums:
#             res = res + [[i] + num for num in res]
#         return res

# 法二，回溯
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTracking(i, temp):
            res.append(temp)
            for j in range(i, len(nums)):
                backTracking(j + 1, temp + [nums[j]])
        backTracking(0, [])
        return res

# 最近重复子问题
# [] --> [1] --> [1,2] [1,3]
# [1,2] --> [1,2,3]

# [] --> [2] --> [2,3]
# [] --> [3]


# @lc code=end

