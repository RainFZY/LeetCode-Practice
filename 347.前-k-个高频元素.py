#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start

# from typing import DefaultDict

# HashMap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        f_order = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        res = []
        for (key, value) in f_order:
            res.append(key)
            if len(res) == k:
                break
        return res

# min-heap
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         frequency = dict()
        
#         for num in nums:
#             value = frequency.get(num)
#             if value is None:
#                 value = 0      
#             frequency[num] = value + 1
            
#         kFrequent = heapq.nlargest(k, frequency.items(), key=lambda x:x[1])
#         elements = [num for num, freq in kFrequent]
        
#         return elements


# @lc code=end

