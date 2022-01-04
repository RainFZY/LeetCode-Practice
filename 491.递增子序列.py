#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
# DFS & 回溯
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(temp, idx):
            # process logic in current level
            if len(temp) >= 2:
                # 判重
                if temp not in res: 
                    res.append(temp[:])
            # DFS
            for i in range(idx, len(nums)):
                # 子序列不递增则跳过当前index
                if temp and nums[i] < temp[-1]: 
                    continue
                else:
                    temp.append(nums[i])
                    dfs(temp, i + 1) # drill down
                    temp.pop()
        dfs([], 0)
        return res


# @lc code=end

