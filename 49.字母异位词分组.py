#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
# 哈希表法，242的升级版
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            hashMap[tuple(sorted(s))] = hashMap.get(tuple(sorted(s)), []) + [s]
        # 把字典的所有value包括到一个数组中返回
        return list(hashMap.values())

# @lc code=end

