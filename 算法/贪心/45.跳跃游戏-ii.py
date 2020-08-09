#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
# 法一，贪心算法，从前向后
# 每次在当前可以跳的范围中，选择下一步能跳最远的位置跳过去
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         # end: 原先最远边界
#         # maxPosition: 新的最远边界
#         end = maxPosition = steps = 0
#         for i in range(len(nums) - 1):
#             maxPosition = max(maxPosition, nums[i] + i)
#             # 跳一步，更新end
#             if i == end:
#                 end = maxPosition
#                 steps += 1
#         return steps

# 法二，贪心算法，从前往后（更易理解的形式）
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        steps = cur = maxPosition = 0
        # 当前还无法跳到最后一个位置，继续循环
        while cur + nums[cur] < len(nums) - 1:
            # 寻找在当前可以跳的范围中，下一步能跳最远的位置
            for i in range(cur + 1, cur + nums[cur] + 1):
                if i + nums[i] > maxPosition:
                    temp = i
                    maxPosition = i + nums[i]
            cur = temp
            steps += 1
        return steps + 1
# @lc code=end

