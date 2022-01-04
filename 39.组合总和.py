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

# DP，类似322零钱兑换
# e.g. target=7可以由target=5的所有结果加上2得到，也可以由target=4的加上3得到...
from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        hashMap = defaultdict(list)
        # 这里两个循环的顺序换一下也可以
        for i in range(1, target+1):
            for j in candidates:
                if i == j:
                    hashMap[i].append([j])
                elif i > j:
                    for k in hashMap[i-j]:
                        temp = k[:]
                        temp.append(j)
                        temp.sort() # 升序，便于后续去重
                        if temp not in hashMap[i]:
                            hashMap[i].append(temp)
        return hashMap[target]





# @lc code=end

