#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
# 哈希表
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for (key, value) in counter.items():
            if value == 1:
                return int(key)

# 异或，难想
# 异或有交换律定理，相当于将相同的数字先异或，这样两两异或就只剩0了，
# 然后0再和最后的一个数字异或得到最终值
# 0 ^ a = a, a ^ a = 0
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res

# 时间复杂度高
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = []
        for i in nums:
            if i not in one:
                one.append(i)
            else:
                one.remove(i)
        return one[0]

# @lc code=end

