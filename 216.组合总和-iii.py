#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
# 回溯，直接套模板即可
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backTrack(start, temp):
            if sum(temp) == n and len(temp) == k:
                res.append(temp[:])
                return
            if sum(temp) > n or len(temp) > k:
                return
            for i in range(start, 10):
                temp.append(i)
                backTrack(i+1, temp)
                temp.pop()
        backTrack(1, [])
        return res
            
# @lc code=end

