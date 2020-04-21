#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         if not board or not board[0] or not words:
#             return []
#         self.result = set()
#         self.end_of_word = "#"

#         # 构建trie
#         root = {}
#         for word in words:
#             node = root
#             for char in word:
#                 node = node.setdefault(char, {})
#             node[self.end_of_word] = "1"
        
#         self.m, self.n = len(board), len(board[0])
#         for i in range(self.m):
#             for j in range(self.n):
#                 if board[i][j] in root:
#                     self.dfs(board, i, j, "", root)
#         return list(self.result)
    
#     def dfs(self, board, i, j, cur_word, cur_dict):
#         cur_word += board[i][j]
#         cur_dict = cur_dict[board[i][j]]
#         # terminator
#         if self.end_of_word in cur_dict:
#             self.result.add(cur_word)
#         temp, board[i][j] = board[i][j], 'visited'
#         for k in range(4):
#             x, y = i + dx[k], j + dy[k]
#             # 判断下一个节点是否越界，判断是否在当前节点的邻结点中且未访问过
#             if 0 <= x < self.m and 0 <= y < self.n and \
#                 board[x][y] != 'visited' and board[x][y] in cur_dict: 
#                 self.dfs(board, x, y, cur_word, cur_dict)
#         board[i][j] = temp


# trie树 + DFS
# 嵌入式写法
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        result = set()
        end_of_word = "#"
        m, n = len(board), len(board[0])

        # 构建trie
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[end_of_word] = "1"
        # 定义 dfs函数
        def dfs(i, j, cur_word, cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            # terminator
            if end_of_word in cur_dict:
                result.add(cur_word)
            # 处理当前层逻辑
            temp, board[i][j] = board[i][j], 'visited'
            for (x, y) in directions:
                temp_x, temp_y = i + x, j + y
                # drill down，判断下一个节点是否越界及是否在当前节点的邻结点中且未访问过
                if 0 <= temp_x < m and 0 <= temp_y < n and \
                    board[temp_x][temp_y] != 'visited' and board[temp_x][temp_y] in cur_dict: 
                    dfs(temp_x, temp_y, cur_word, cur_dict)
            # 恢复当前层状态
            board[i][j] = temp
        # 调用dfs函数
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, "", root)
        return list(result)
    


# @lc code=end

