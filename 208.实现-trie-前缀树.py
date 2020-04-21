#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
# 用字典嵌套的方式实现，每个节点对应一个字典，key存放该节点的子节点，value对应子节点的字典
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#" # 自定义

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root # 字典，对于每个node，key是字母，value是一个字典（字典套字典）
        # 遍历word中的每一个字母
        for char in word:
            # dict.setdefault(key, default=None)
            # key:查找的键值。default:键不存在时，设置的默认键值。
            # 如果字典的key包含有char，则返回char这个key对应的value，
            # 即node变成这个value表示的的字典，否则返回{}（这样node实现迭代向下，知道最下面的节点）
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word # value值随意定

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

