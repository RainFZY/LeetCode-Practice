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


# @lc code=end

