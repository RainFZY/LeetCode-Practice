#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
# 法一，利用set查找只要O(1)的特点，降低时间复杂度
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = set(nums)
        n = len(nums)
        res = []
        for i in range(1, n + 1):
            if i not in counter:
                res.append(i)
        return res



# 原地算法：
# 将所有正数作为数组下标，置对应数组值为负值。那么，仍为正数的位置即为（未出现过）消失的数字。
# 举个例子：
# 原始数组：[4,3,2,7,8,2,3,1]
# 重置后为：[-4,-3,-2,-7,8,2,-3,-1]
# 结论：[8,2] 分别对应的index为[5,6]（消失的数字）
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        res = []
        for (i,num) in enumerate(nums):
            if num > 0:
                res.append(i+1)
        return res
        # 高级return法
        # return [i + 1 for i, num in enumerate(nums) if num > 0]

# @lc code=end

