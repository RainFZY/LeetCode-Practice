#
# @lc app=leetcode.cn id=1268 lang=python3
#
# [1268] 搜索推荐系统
#

# @lc code=start
# 字典树
class Solution:
    def __init__(self):
        self.trie = DefaultDict(list) # 因为要返回list，所以初始化为list型

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 往字典树里面insert，嵌套形式
        def addWord(root, word):
            cur = root
            for ch in word:
                if ch not in cur:
                    cur[ch] = DefaultDict(list)
                cur = cur[ch]
                cur["words"].append(word)
                cur["words"].sort() # 按字母顺序排序
                if len(cur["words"]) > 3:
                    cur["words"].pop()

        root = self.trie
        # 先构建字典树
        for word in products:
            addWord(root, word)
        
        res = list()
        cur = root
        flag = False
        # 再查找
        for ch in searchWord:
            if flag or ch not in cur:
                res.append(list())
                # 一旦有一个字母匹配不到，之后的都匹配不到，输出[]
                flag = True
            else:
                cur = cur[ch]
                res.append(cur["words"])

        return res
# @lc code=end

