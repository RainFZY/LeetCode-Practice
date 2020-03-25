#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
# 排序 + 一次扫描
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        n = len(intervals)
        res = []
        left, right = intervals[0][0], intervals[0][1]
        for i in range(n):
            if intervals[i][0] <= right and intervals[i][1] > right:
                right = intervals[i][1]
            elif intervals[i][0] > right:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        res.append([left, right])
        return res
                
# @lc code=end

