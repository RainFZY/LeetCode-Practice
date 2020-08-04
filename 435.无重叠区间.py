#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
# 贪心算法：
# 每次保留的时候，选择左端点跟前面的已经覆盖的区间不重合的，右端点又尽量小（通过排序实现）的保留
# 1、从区间集合 intvs 中选择一个区间 x，这个 x 是在当前所有区间中结束最早的（end 最小）。
# 2、把所有与 x 区间相交的区间从区间集合 intvs 中删除。
# 3、重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        cur_end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < cur_end:
                count += 1
            else:
                cur_end = intervals[i][1]
        return count
# @lc code=end

