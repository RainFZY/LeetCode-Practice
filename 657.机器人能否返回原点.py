#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("R") == moves.count("L") and \
            moves.count("U") == moves.count("D"):
            return True
        else:
            return False
# @lc code=end

