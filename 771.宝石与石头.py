#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for s in S:
            if s in J:
                cnt += 1
        return cnt

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        for s in J:
            cnt += S.count(s)
        return cnt
# @lc code=end

