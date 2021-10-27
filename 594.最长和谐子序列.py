#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
# HashMap
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        res = 0
        for num in nums:
            if hashMap.get(num+1):
                res = max(res, hashMap.get(num+1) + hashMap.get(num))
        return res

# @lc code=end

