#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
# 法一，哈希表【推荐】
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashMap = {}
        n = len(nums)
        for i in range(n):
            hashMap[nums[i]] = nums[i]
        for i in range(1, n + 1):
            if not hashMap.get(i):
                return i
        return n + 1

# 法二
# 要找的数一定是在[1, N+1]里的整数
# 把1放在下标为0的位置上，把2放在下标为1的位置...
# 找到最小的没有放置正确数字的下标
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                index1, index2 = i, nums[i] - 1
                # 交换至正确的位置上
                nums[index1], nums[index2] = nums[index2], nums[index1]
        # 找到最小的没有放置正确数字的下标
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        return n + 1


# @lc code=end

