#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
# 将字符串 s 按照 00 和 11 的连续段分组，存在counts数组中
# e.g. s = '00111011', count = [2,3,1,2]
# res = min(2,3) + min(3,1) + min(1,2)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        j = 0
        count = [1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count[j] += 1
            else:
                count.append(1)
                j += 1
        res = 0
        for i in range(1, len(count)):
            res += min(count[i], count[i-1])
        return res


# @lc code=end

