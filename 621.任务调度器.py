#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
# https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        print(counter)
        m = 0   # 最大任务数量
        c = 0   # 最大任务数量的个数
        for v in counter.values():
            if v > m:
                m = v
                c = 1
            elif v == m:
                c += 1
        return max(len(tasks), (n + 1) * (m - 1) + c)
# @lc code=end

