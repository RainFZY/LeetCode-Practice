#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
# 法一，哈希表
# O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for num in nums:
            if hashMap.get(num):
                hashMap[num] += 1
            else:
                hashMap[num] = 1
            if hashMap[num] > len(nums)/2:
                return num

# 法二，排序法
# O(nlogn)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums)//2]

# 法三，分治
# O(nlogn)
# 我们使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。
# 长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
# 如果回溯后某区间的长度大于 1，我们必须将左右子区间的值合并。
# 如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
# 否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数
# class Solution:
#     def majorityElement(self, nums, lo=0, hi=None):
#         def majority_element_rec(lo, hi):
#             # base case; the only element in an array of size 1 is the majority
#             # element.
#             if lo == hi:
#                 return nums[lo]

#             # recurse on left and right halves of this slice.
#             mid = (hi-lo)//2 + lo
#             left = majority_element_rec(lo, mid)
#             right = majority_element_rec(mid+1, hi)

#             # if the two halves agree on the majority element, return it.
#             if left == right:
#                 return left

#             # otherwise, count each element and return the "winner".
#             left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
#             right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

#             return left if left_count > right_count else right

#         return majority_element_rec(0, len(nums)-1)




# @lc code=end

