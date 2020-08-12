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
        # 法一
        # dict.values()：以列表返回字典中的所有值，字符串形式
        print(hashMap.values())
        return list(hashMap.values())
        # 法二
        # res = []
        # dict.items() --> 以列表返回可遍历的(键, 值) 元组数组
        # for (key, value) in hashMap.items():
        #     res.append(value)
        # return res
# @lc code=end

