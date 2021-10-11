#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
# HashMap
# key: value = char: freq
class Solution:
    def frequencySort(self, s: str) -> str:
        frequencyMap = {}
        for char in s:
            frequencyMap[char] = frequencyMap.get(char, 0) + 1
        f_oder = sorted(frequencyMap.items(), key=lambda x: x[1], reverse=True)
        res = ''
        for (char, freq) in f_oder:
            res += char*int(freq)
        return res

# HashMap
# key: value = freq: char
# 这样的好处是key和value可能是1对多，减少了key的数量，sort时更快
class Solution:
    def frequencySort(self, s: str) -> str:
        frequencyMap = {}
        for char in s:
            frequencyMap[char] = frequencyMap.get(char, 0) + 1
        reverseMap = {}
        for (char, freq) in frequencyMap.items():
            reverseMap[freq] = reverseMap.get(freq, [])
            reverseMap[freq].append(char)
        f_oder = sorted(reverseMap.items(), key=lambda x: x[0], reverse=True)
        res = ''
        for (freq, char) in f_oder:
            for i in range(len(char)):
                res += char[i]*int(freq)
        return res
# @lc code=end

