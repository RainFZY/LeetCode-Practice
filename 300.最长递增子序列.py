#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
# 法一：DP + 双指针
# 状态定义成：dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度
# 状态转移方程：dp[i]= max(dp[j]+1)，其中 0≤j<i，nums[j]<nums[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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


# DP优化（贪心 + 二分查找），较为巧妙，动画见：
# https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         # 特判
#         if n < 2:
#             return n

#         # 为了防止后序逻辑发生数组索引越界，先把第 1 个数放进去
#         tail = [nums[0]]
#         for i in range(1, n):
#             # 【逻辑 1】比 tail 数组实际有效的末尾的那个元素还大
#             # 先尝试是否可以接在末尾
#             if nums[i] > tail[-1]:
#                 tail.append(nums[i])
#                 continue

#             # 使用二分查找法，在有序数组 tail 中
#             # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小，更新tail
#             left = 0
#             right = len(tail) - 1
#             while left < right:
#                 # 选左中位数不是偶然，而是有原因的，原因请见 LeetCode 第 35 题题解
#                 # mid = left + (right - left) // 2
#                 mid = (left + right) >> 1
#                 if tail[mid] < nums[i]:
#                     # 中位数肯定不是要找的数，把它写在分支的前面
#                     left = mid + 1
#                 else:
#                     right = mid
#             # 走到这里是因为【逻辑 1】的反面，因此一定能找到第 1 个大于等于 nums[i] 的元素，因此无需再单独判断
#             tail[left] = nums[i]
#         return len(tail)
# @lc code=end

