#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
# 法一，暴力，超时
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        res = float('inf')
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= s:
                    res = min(res, j - i + 1)
                    break
        return 0 if res == float('inf') else res

# 法二，滑动窗口/双指针
# 扩张窗口：为了找到一个可行解，找到了就不再扩张
# 收缩窗口：在长度上优化该可行解，直到条件被破坏
# 寻找下一个可行解，然后再优化到不能优化……
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        res = float('inf')
        start, end = 0, 0
        total = 0
        # 主循环扩张
        while end < n:
            total += nums[end]
            # 次循环收缩
            while total >= s:
                res = min(res, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if res == float('inf') else res

# 法三，前缀和 + 二分查找（调库）
# 额外创建一个数组 sums 用于存储数组 nums 的前缀和，其中 sums[i] 表示从 
# nums[0] 到 nums[i−1] 的元素和
# class Solution:
#     def minSubArrayLen(self, s: int, nums: List[int]) -> int:
#         if not nums:
#             return 0
        
#         n = len(nums)
#         ans = n + 1
#         sums = [0]
#         for i in range(n):
#             sums.append(sums[-1] + nums[i])
        
#         for i in range(1, n + 1):
#             target = s + sums[i - 1]
#             bound = bisect.bisect_left(sums, target)
#             if bound != len(sums):
#                 ans = min(ans, bound - (i - 1))
        
#         return 0 if ans == n + 1 else ans
# @lc code=end

