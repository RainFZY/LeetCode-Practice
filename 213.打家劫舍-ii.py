#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
# DP
# 第一个房子和最后一个房子中只能选择一个偷窃
# 把此环状排列房间问题约化为两个单排排列房间子问题：
# 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1
# 在不偷窃最后一个房子的情况下（即 nums[:n-1]），最大金额是 p2 
# 综合偷窃最大金额：为以上两种情况的较大值，即 max(p1,p2)
# 单排排列房间子问题同198，直接调用函数

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def sub_rob(nums: List[int]) -> int:
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return max(dp)
            
        return max(sub_rob(nums[1:]), sub_rob(nums[:-1]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub_rob(nums: List[int]) -> int:
            if not nums:
                return 0
            n = len(nums)
            # 构建n * 2的二维数组
            #   第几行代表第几个房屋的情况
            #   第一列代表不偷这个房子的收入，第二列代表偷的收入
            array = [[0] * 2 for _ in range(n)]
            array[0][1] = nums[0]
            for i in range(1, n):
                array[i][0] = max(array[i - 1][0], array[i - 1][1])
                array[i][1] = array[i - 1][0] + nums[i]
            return max(array[n - 1][0], array[n - 1][1])

        return max(sub_rob(nums[:-1]), sub_rob(nums[1:])) if len(nums) != 1 else nums[0]
# @lc code=end

