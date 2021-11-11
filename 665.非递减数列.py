#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)
        count = 0
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                count += 1
                # 提前剪枝
                if count > 1:
                    return False
                # 把前面的数变小
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                # 把后面的数变大
                else:
                    nums[i] = nums[i - 1]
        return True
# @lc code=end

