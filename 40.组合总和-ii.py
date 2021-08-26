#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
# 回溯
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def backTrack(start, temp):
            if sum(temp) > target:
                return
            elif sum(temp) == target:
                res.append(temp[:])
                return
            else:
                for i in range(start, len(candidates)):
                    # 如果从index开始的数有连续出现的重复数字，
                    # 跳过该数字continue，因为这会产生重复解
                    # 比如[1, 1, 2, 5, 6, 7, 10], 避免两个[1, 2, 5]出现
                    # 但是可以保证[1, 1, 6]合法，仔细品品
                    # 这一句没想到
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    temp.append(candidates[i])
                    backTrack(i+1, temp)
                    temp.pop()
        backTrack(0, [])
        return res
 # @lc code=end

