#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
# 双指针法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            res = max(area, res)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return res
# @lc code=end

