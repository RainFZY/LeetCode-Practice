#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力解法，结果超出时间限制。。。
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         j += 1
        #     i += 1
        # return []


        # 用字典模拟哈希查询
        # harshmap = {}
        # for ind,num in enumerate(nums):
        #     harshmap[num] = ind # 因为要找的是num的值，所以num作为key，以便调用get函数
        # for i,num in enumerate(nums):
        #     j = harshmap.get(target - num) # get key，返回value
        #     if j is not None and i != j:
        #         return [i,j]


        # 哈希表法二
        harshmap = {}
        for i, num in enumerate(nums):
            if target - num in harshmap:
                return(i, harshmap[target - num])
            harshmap[num] = i
            








# @lc code=end

