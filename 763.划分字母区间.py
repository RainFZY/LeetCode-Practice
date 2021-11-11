#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
# 贪心
# https://leetcode-cn.com/problems/partition-labels/solution/dai-ma-sui-xiang-lu-dai-ni-xue-tou-tan-x-czmo/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        # 统计每一个字符最后出现的位置
        for i in range(len(s)):
            hashMap[s[i]] = i
        result = []
        left, right = 0, 0
        for i in range(len(s)):
            right = max(right, hashMap[s[i]])
            # 如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点了
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result
# @lc code=end

