#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
# BFS
# from collections import defaultdict
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if not beginWord or not endWord or not wordList or endWord not in wordList:
#             return 0
#         # 所有词都相同长度
#         n = len(beginWord)
#         # 初始化过渡词字典
#         all_combo_dict = defaultdict(list)
#         for word in wordList:
#             for i in range(n):
#                 all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
        
#         queue = [(beginWord, 1)]
#         visited = {beginWord: True}
#         while queue:
#             # 取出头部的，先进先出
#             current_word, level = queue.pop(0)
#             for i in range(n):
#                 # 过渡词（差一个字母）
#                 intermediate_word = current_word[:i] + "*" + current_word[i+1:]
#                 for word in all_combo_dict[intermediate_word]:
#                     if word == endWord:
#                         return level + 1
#                     if word not in visited:
#                         visited[word] = True
#                         queue.append((word, level + 1))
#                 all_combo_dict[intermediate_word] = []
#         return 0


# BFS，简洁版
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        # 所有词都相同长度
        n = len(beginWord)
        queue = [(beginWord, 1)]
        wordList = set(wordList)
        while queue:
            # 取出头部的，先进先出
            current_word, level = queue.pop(0)
            for i in range(n):
                # 'a' --> 'z'
                for c in string.ascii_lowercase:
                    # 过渡词（差一个字母）
                    intermediate_word = current_word[:i] + c + current_word[i+1:]
                    if intermediate_word == endWord:
                        return level + 1
                    if intermediate_word in wordList:
                        queue.append((intermediate_word, level + 1))
                        wordList.remove(intermediate_word)
        return 0


# # 法二，双向BFS
# # 不用 queue 用 set
# import string
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
#         front = {beginWord}
#         back = {endWord}
#         dist = 1
#         wordList = set(wordList)
#         word_len = len(beginWord)
#         while front:
#             dist += 1
#             next_front = set()
#             for word in front:
#                 for i in range(word_len):
#                     # 'a' --> 'z'
#                     for c in string.ascii_lowercase:
#                         if c != word[i]:
#                             # 所有的过渡词（差一个字母）
#                             new_word = word[:i] + c + word[i+1:]
#                             if new_word in back:
#                                 return dist
#                             if new_word in wordList:
#                                 next_front.add(new_word)
#                                 wordList.remove(new_word)
#             front = next_front
#             if len(back) < len(front):
#                 front, back = back, front
#         return 0
# @lc code=end

