#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
# 回溯
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTrack(start, temp):
            if sum(temp) == target:
                res.append(temp[:]) # 一定别漏了[:]
                return
            elif sum(temp) > target:
                return
            else:
                for i in range(start, len(candidates)):
                    temp.append(candidates[i])
                    backTrack(i, temp) # 把下一个start设成i，表示可以重复读取当前的数
                    temp.pop()
        backTrack(0, [])
        return res




# @lc code=end

