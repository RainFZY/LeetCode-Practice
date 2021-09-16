#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
# 双指针
class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        arr = list(s) # 字符串操作不方便，先转数组
        # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = set(list('aeiouAEIOU')) # 这样写更方便些
        while left < right:
            if arr[left] in vowels and arr[right] not in vowels:
                right -= 1
            elif arr[left] not in vowels and arr[right] in vowels:
                left += 1
            elif arr[left] not in vowels and arr[right] not in vowels:
                left += 1
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        s = ''.join(arr)
        return s
                

# @lc code=end

