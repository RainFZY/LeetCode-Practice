#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
# 法一，调库函数
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         return sorted(nums)

# 法二，快排
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         self.quickSort(nums, 0, len(nums) - 1)
#         return nums

#     def quickSort(self, array, begin, end):
#         if end <= begin:
#             return
#         pivot = self.partition(array, begin, end)
#         self.quickSort(array, begin, pivot - 1)
#         self.quickSort(array, pivot + 1, end)

#     def partition(self, array, begin, end):
#         pivot = end
#         counter = begin
#         for i in range(begin, end):
#             if array[i] < array[pivot]:
#                 array[i], array[counter] = array[counter], array[i]
#                 counter += 1
#         array[counter], array[pivot] = array[pivot], array[counter]
#         return counter

# 法三，归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def mergeSort(self, array, left, right):
        if left >= right:
            return
        mid = left + (right - left) // 2
        self.mergeSort(array, left, mid)
        self.mergeSort(array, mid + 1, right)
        self.merge(array, left, mid, right)
    
    def merge(self, array, left, mid, right):
        i, j = left, mid + 1
        temp = []
        while i <= mid or j <= right:
            if i > mid or (j <= right and array[j] < array[i]):
                temp.append(array[j])
                j += 1
            else:
                temp.append(array[i])
                i += 1
        array[left: right + 1] = temp 


# @lc code=end

