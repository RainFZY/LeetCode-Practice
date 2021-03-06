#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
# 滑动窗口 + 哈希表
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        cur_len = 0
        n = len(s)
        hashMap = []
        for i in range(n):
            # 出现重复字符
            if s[i] in hashMap:
                # 该字符上一次出现的位置下标
                index = hashMap.index(s[i])
                # 截取该字符之后的子串（滑动窗口左边移动）
                hashMap = hashMap[index + 1:]
                hashMap.append(s[i])
                cur_len = len(hashMap)
            # 该字符不是重复字符
            else:
                cur_len += 1
                # 滑动窗口右边移动
                hashMap.append(s[i])
            if cur_len > max_len:
                max_len = cur_len

        return max_len

# @lc code=end

