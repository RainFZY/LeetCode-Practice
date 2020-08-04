#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
# 法一，迭代
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
# 第一个循环：[] --> [], [1]
# 第二个循环：[], [1] --> [], [1], [2], [1, 2]
# 第三个循环：[], [1], [2], [1, 2] --> [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]

# 法二，回溯
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTracking(i, temp):
            # terminator
            if i > len(nums):
                return 
            # process
            res.append(temp)
            # drill down
            for j in range(i, len(nums)):
                backTracking(j + 1, temp + [nums[j]])
            # 无reverse state
        backTracking(0, [])
        return res

# 最近重复子问题
# [] --> [1] --> [1,2] [1,3]
# [1,2] --> [1,2,3]

# [] --> [2] --> [2,3]
# [] --> [3]


# @lc code=end

