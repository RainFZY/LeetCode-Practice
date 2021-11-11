#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
# Binary Search
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters)-1
        while left <= right:
            mid = left + (right - left) // 2
            # 因为可能出现字母重复，所以letters[mid]==target时不急着return
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return letters[left] if left < len(letters) else letters[0]

# 法二
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            # 直接letter > target也行
            if ord(letter) > ord(target):
                return letter
        return letters[0]
# @lc code=end

