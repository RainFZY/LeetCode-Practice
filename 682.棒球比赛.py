#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
# 最近相关性（最后一轮） --> 栈
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in range(len(ops)):
            if ops[i] == "C":
                res.pop()
            elif ops[i] == "D":
                res.append(2 * res[-1])
            elif ops[i] == "+":
                res.append(res[-1] + res[-2])
            # 对于if条件比较难描述的，可以放到else中来，就不用描述了
            else:
                res.append(int(ops[i]))
        return sum(res)
# @lc code=end

