#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    # 巧妙
    # https://leetcode-cn.com/problems/trapping-rain-water/solution/wei-en-tu-jie-fa-zui-jian-dan-yi-dong-10xing-jie-j/
    def trap(self, height: List[int]) -> int:
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(len(height)):
            max1 = max(height[i], max1)
            s1 += max1
        for i in range(len(height)-1, -1, -1):
            max2 = max(height[i], max2)
            s2 += max2
        res = s1 + s2 - len(height) * max1 - sum(height)
        return res
# @lc code=end

