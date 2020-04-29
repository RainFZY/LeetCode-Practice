#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    # 对于每一个未填的位置，遍历每个数字，依次检查是否可以填
                    for char in ['1','2','3','4','5','6','7','8','9']:
                        if self.isValid(board, i, j, char):
                            board[i][j] = char
                            # 看放上char后是否合法
                            if self.solveSudoku(board):
                                 return True
                            # 若不合法，说明不能放这个char，则返回原始状态，剪枝
                            else:
                                board[i][j] = '.'
                    return False
        return True

    # 判断是否合法
    def isValid(self, board, row, col, char):
        for i in range(9):
            # 检查行
            if board[i][col] != '.' and board[i][col] == char:
                return False
            # 检查列
            if board[row][i] != '.' and board[row][i] == char:
                return False
            # 检查九宫格
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] != '.' and \
                board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
                return False
        return True
# @lc code=end

