#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
# greedy，类似435
# 按照Xend从小到大排序
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 按照Xend从小到大排序
        points.sort(key=lambda x: x[1])
        cnt = 1
        for i in range(1, len(points)):
            if points[i][0] <= points[i-1][1]:
                points[i] = [max(points[i-1][0], points[i][0]), points[i-1][1]]
            else:
                cnt += 1
        return cnt

# @lc code=end

