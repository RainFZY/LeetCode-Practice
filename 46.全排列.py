#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
# 无重复数组
# 回溯
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backTracking(nums, temp):
            # terminator
            if len(temp) == n:
                res.append(temp)
                return
            # drill down
            for i in range(len(nums)):
                # 若nums[:0]返回的是[]
                # nums在这里的作用就是把temp中加入的那个数在可选中给去掉
                backTracking(nums[:i] + nums[i+1:], temp + [nums[i]])
        backTracking(nums,[])
        return res

# 复习，current level + drill down + reverse标准写法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(num, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(num)):
                cur = num[i]
                temp.append(cur)
                # nums.remove(nums[i])
                num = num[:i] + num[i+1:]
                backTrack(num, temp)
                temp.pop()
                num.insert(i, cur)
        backTrack(nums, [])
        return res
# @lc code=end

