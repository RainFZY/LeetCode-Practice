#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
# 双指针，类似26
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in nums:
            if right != val:
                nums[left] = right
                left += 1
        return left




# @lc code=end

