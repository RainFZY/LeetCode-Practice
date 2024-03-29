#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start

# 一维DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = nums
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        res = dp[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # res = max(res, dp[i])
        res = max(dp)
        return res

# 最简版，改写法一
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         preMax, curMax = 0, 0
#         for num in nums:
#             # 同步计算，并不是curMax更新完马上赋给preMax，这样就相当于不能偷相邻的
#             curMax, preMax = max(preMax + num, curMax), curMax
#         return curMax

# 二维DP，增加一维以存储偷或不偷的状态
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # 构建n * 2的二维数组
        # 第几行代表第几个房屋的情况
        # 第一列代表不偷这个房子的收入，第二列代表偷的收入
        array = [[0] * 2 for _ in range(n)]
        array[0][1] = nums[0]
        for i in range(1, n):
            array[i][0] = max(array[i - 1][0], array[i - 1][1])
            array[i][1] = array[i - 1][0] + nums[i]
        return max(array[n - 1][0], array[n - 1][1])



# @lc code=end

