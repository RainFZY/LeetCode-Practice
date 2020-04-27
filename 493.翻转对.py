#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
# 法一，暴力法，超时
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         res = 0
#         for j in range(len(nums)):
#             for i in range(j):
#                 if nums[i] > 2 * nums[j]:
#                     res += 1
#         return res

# 法二，归并排序
# 同逆序对的做法
# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
#         self.cnt = 0
#         self.mergeSort(nums, 0, len(nums) - 1)
#         return self.cnt

#     def mergeSort(self, array, left, right):
#         if left >= right:
#             return
#         mid = left + (right - left) // 2
#         self.mergeSort(array, left, mid)
#         self.mergeSort(array, mid + 1, right)
#         self.merge(array, left, mid, right)
    
#     def merge(self, array, left, mid, right):
#         # 专门循环一遍来统计 cnt，不能跟merge的混在一起
#         i, j = left, mid + 1
#         while i <= mid and j <= right:
#             if array[i] > 2 * array[j]:
#                 self.cnt += mid - i + 1
#                 j += 1
#             else:
#                 i += 1
#         # 新建数组merge排序
#         i, j = left, mid + 1
#         temp = []
#         while i <= mid and j <= right:
#             if array[i] <= array[j]:
#                 temp.append(array[i])
#                 i += 1
#             else:
#                 temp.append(array[j])
#                 j += 1
#         # 补余
#         while i <= mid:
#             temp.append(array[i])
#             i += 1
#         while j <= right:
#             temp.append(array[j])
#             j += 1
#         array[left: right + 1] = temp 
        
    
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergeSort(nums, 0, len(nums) - 1)
        return self.cnt

    def mergeSort(self, array, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(array, left, mid)
        self.mergeSort(array, mid + 1, right)
        self.merge(array, left, mid, right)
    
    def merge(self, array, left, mid, right):
        i, j = left, mid + 1
        while i <= mid and j <= right:
            if array[i] > 2 * array[j]:
                self.cnt += mid - i + 1
                j += 1
            else:
                i += 1
        # 偷了个懒，把 merge部分的代码用sort函数直接替代
        array[left: right + 1] = sorted(array[left: right + 1])

  
# @lc code=end

