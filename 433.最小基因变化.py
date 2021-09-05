#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
# BFS，同127单词接龙
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or not bank or end not in bank:
            return -1
        # 所有词都相同长度
        n = len(start)
        queue = [(start, 1)]
        while queue:
            # 取出头部的，先进先出
            current_word, level = queue.pop(0)
            # 两层循环，尝试所有的替换情况
            for i in range(n):
                for c in ['A', 'C', 'G', 'T']:
                    # 过渡词（差一个字母）
                    intermediate_word = current_word[:i] + c + current_word[i+1:]
                    if intermediate_word == end:
                        return level
                    if intermediate_word in bank:
                        queue.append((intermediate_word, level + 1))
                        bank.remove(intermediate_word)
        return -1

# 复习
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or not bank or end not in bank:
            return -1
        n = len(start)
        # bank = set(bank)
        queue = [(start, 1)]
        while queue:
            (cur, level) = queue.pop(0)
            for i in range(n):
                for c in ["A", "C", "G", "T"]:
                    intermediate_gene = cur[:i] + c + cur[i+1:]
                    if intermediate_gene == end:
                        return level
                    if intermediate_gene in bank:
                        bank.remove(intermediate_gene)
                        queue.append((intermediate_gene, level+1))
        return -1
# @lc code=end

