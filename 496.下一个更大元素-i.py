#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
# 法一：暴力法 O(n^2)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m = len(nums1), len(nums2)
        res = [-1] * n
        for i in range(n):
            if nums2.count(nums1[i]):
                start = nums2.index(nums1[i])
                for j in range(start+1, m):
                    if nums2[j] > nums1[i]:
                        res[i] = nums2[j]
                        break
        return res

# 法二：哈希表 + 单调栈
# 先遍历 nums2，对 nums2 中的每一个元素，求出其右边第一个更大的元素
# 利用单调栈来找每个元素右边第一个更大的元素，栈内元素保持单调递减
# 这样每遇到一个更大的，栈顶元素不断出栈，直到重新变成单调递减
# 将对应关系放入哈希表中，之后遍历 nums1 就可以直接在哈希表中找
# 动画：官方题解 https://leetcode-cn.com/problems/next-greater-element-i/solution/xia-yi-ge-geng-da-yuan-su-i-by-leetcode/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashMap = {}
        res = []
        # 避免了两个循环
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hashMap[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        while stack:
            hashMap[stack.pop()] = -1
        for i in range(len(nums1)):
            res.append(hashMap[nums1[i]])
        return res 
# @lc code=end

