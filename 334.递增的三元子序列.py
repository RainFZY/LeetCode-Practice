#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
# 法一，贪心（类似单调栈思想）
# 按顺序遍历数组，维护一个small和一个mid，遇到比 small 小的，
# 就把 small 换成更小的，遇到比 middle 小的，就把 middle 换成更小的
# 当碰到比它们都大的时，就找到了递增的三元子序列
# 这种方法只能解决存在不存在这样的递增子序列，但最后 small 和 middle 中存储的并不一定是子序列
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = mid = inf
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False


# 用300 最长上升子序列 的函数，返回输入数组的最长上升子序列的长度
# O(n^2)，超时
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def lengthOfLIS(nums):
            if not nums:
                return 0
            n = len(nums)
            dp = [1] * n
            # 双指针遍历所有片段
            for i in range(n):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return max(dp)
        max_len = lengthOfLIS(nums)
        return max_len >= 3

# 300 最长上升子序列，单调栈 + 二分查找（调库）
# O(nlogn)，通过
import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def lengthOfLIS(nums):
            stack = [] # 维护一个单调递增栈
            for num in nums:
                # idx: num应该插入在stack中的位置，往左取
                idx = bisect.bisect_left(stack, num)
                if idx == len(stack):
                    stack.append(num)
                else:
                    stack[idx] = num
            return len(stack)
        max_len = lengthOfLIS(nums)
        return max_len >= 3
# @lc code=end

