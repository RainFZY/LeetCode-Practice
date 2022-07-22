#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
# greedy，类似435
# 按照Xend从小到大排序
# [1,6], [2,8], [7, 12], [10, 16]
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 按照Xend从小到大排序
        points.sort(key=lambda x: x[1])
        cnt = 1
        for i in range(1, len(points)):
            # 有重叠区间
            if points[i][0] <= points[i-1][1]:
                points[i] = [max(points[i-1][0], points[i][0]), points[i-1][1]]
            # 无重复区间，就得多射一箭
            else:
                cnt += 1
        return cnt

# @lc code=end

