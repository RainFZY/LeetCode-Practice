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
        # 回溯
        def helper(i, j, cnt, visited):
            # terminator
            if cnt == len(word):
                return True
            # process
            for (x, y) in directions:
                temp_i = i + x
                temp_j = j + y
                if 0 <= temp_i < row and 0 <= temp_j < col and (temp_i, temp_j) \
                    not in visited and board[temp_i][temp_j] == word[cnt]:
                    visited.add((temp_i, temp_j))
                    # drill down，如果这个节点能到底，就 return
                    if helper(temp_i, temp_j, cnt+1, visited):
                        return True
                    # 不能到底，清理，reverse the current state
                    visited.remove((temp_i, temp_j))
            return False
        
        for i in range(row):
            for j in range(col):
                # 第一个字母单独判断，因此cnt从1开始不是从0开始
                if board[i][j] == word[0] and helper(i, j, 1, {(i, j)}):
                    return True
        return False

# 复习，基本完全没写出来，比一般的回溯要复杂很多
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        cnt, visited = 0, []
        def backTrack(i, j, cnt, visited):
            if cnt == len(word):
                return True
            for (x, y) in directions:
                temp_x, temp_y = i + x, j + y
                if 0 <= temp_x < len(board) and 0 <= temp_y < len(board[0]) and \
                    (temp_x, temp_y) not in visited and board[temp_x][temp_y] == word[cnt]:
                    visited.add((temp_x, temp_y))
                    if backTrack(i+x, j+y, cnt+1, visited):
                        return True
                    visited.remove((temp_x, temp_y))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and backTrack(i, j, 1, {(i, j)}):
                    return True
        return False

# @lc code=end

