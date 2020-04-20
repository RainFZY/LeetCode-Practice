#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
# 回溯 + DFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(board)
        col = len(board[0])
        def helper(i, j, cnt, visited):
            if cnt == len(word):
                return True
            for (x, y) in directions:
                temp_i = i + x
                temp_j = j + y
                if 0 <= temp_i < row and 0 <= temp_j < col and (temp_i, temp_j) \
                not in visited and board[temp_i][temp_j] == word[cnt]:
                    visited.add((temp_i, temp_j))
                    # 这个节点可以，它的下一个节点也要可以，不然就回溯
                    if helper(temp_i, temp_j, cnt+1, visited):
                        return True
                    # 回溯
                    visited.remove((temp_i, temp_j))
            return False
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
                    return True
        return False


# @lc code=end

