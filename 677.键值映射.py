#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

# @lc code=start
# 字典树 Trie
class MapSum:

    def __init__(self):
        self.trie = defaultdict(int) # 主树
        self.history = defaultdict(int) # 记录是否有重复key输入

    def insert(self, key: str, val: int) -> None:
        diff = val - self.history[key]
        self.history[key] = val
        cur = self.trie
        for char in key:
            cur.setdefault(char, defaultdict(int)) # 用setdefault函数
            # if char not in cur:
            #     cur[char] = defaultdict(int)
            cur = cur[char]
            cur["sum"] += diff

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for char in prefix:
            if char not in cur:
                return 0
            cur = cur[char]
        return cur["sum"]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

