#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# Binary Search
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        while left < right: # left == right时会无限循环
            mid = left + (right - left) // 2
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
        return left

        
# @lc code=end

