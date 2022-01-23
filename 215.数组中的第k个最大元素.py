#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
# 耍赖法
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

# Max Heap，大顶堆
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        # heapq.heapify(heap)
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            # 维护大小为k的堆
            if len(heap) > k:
                heapq.heappop(heap) # pop最小值，即pop heap[0]
            print(heap)
        # 返回k个最大元素中最小的那个
        return heap[0]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [] #创建一个空堆
        for i in nums:
            # python 本身仅支持小根堆，通过加‘-’号构建大根堆
            heapq.heappush(maxHeap, -i) 
        for _ in range(k - 1): # 弹出前k-1个item
            heapq.heappop(maxHeap)
        # 输出为第k小的item，并乘‘-’恢复成第k大
        return -maxHeap[0] 

# Quick Sort
from random import randrange
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums, 0, len(nums)-1, k)
    def quickSort(self, a, begin, end, k):
        if begin > end:
            return
        pivot = self.partition(a, begin, end)
        if (end - pivot + 1) == k:
            return a[pivot]
        elif (end - pivot + 1) < k:
            return self.quickSort(a, begin, pivot-1, k-(end-pivot+1))
        else:
            return self.quickSort(a, pivot+1, end, k)

    def partition(self, a, begin, end):
        # pivot = randrange(begin, end+1) # 避免一直在最差情况 → O(n^2)
        pivot = end
        print(pivot)
        cnt = begin
        for i in range(begin, end):
            if a[i] < a[pivot]:
                a[i], a[cnt] = a[cnt], a[i]
                cnt += 1
        a[pivot], a[cnt] = a[cnt], a[pivot]
        return cnt


# @lc code=end

