#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
# 贪心算法（从后往前）
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        # 最后的能跳到的点
        endReachable = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= endReachable:
                endReachable = i
        return endReachable == 0
# @lc code=end

