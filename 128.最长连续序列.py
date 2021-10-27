#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
# O(n), set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in nums:          
            if i-1 in numSet:
                # 只记+的，-1的若有之后也会遍历到
                continue
            else:
                cnt = 1
                while i+cnt in numSet:
                    cnt += 1
                res = max(res,cnt)
        return res
# @lc code=end

