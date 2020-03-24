#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
# 暴力法
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = 0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    arr1[count], arr1[j] = arr1[j], arr1[count]
                    count += 1
        print(sorted(arr1[count:]))
        arr1[count:] = sorted(arr1[count:])
        return arr1
# @lc code=end

