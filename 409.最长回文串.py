#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
# 统计每个字母出现的次数，若为偶数，则刚好可以分配到两边
# 若为奇数，则减一后分配到两边
# 最后中间那个数有没有取决于是否有奇数
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = defaultdict(int)
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        res = 0
        exist_odd = 0
        for (key, value) in hashMap.items():
            if value % 2 == 1:
                value -= 1
                exist_odd = 1
            res += value
        return res + exist_odd
# @lc code=end

