#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
# 法一
# 模拟螺旋矩阵的路径。初始位置是矩阵的左上角，初始方向是向右，
# 当路径超出界限或者进入之前访问过的位置时，则顺时针旋转，进入下一个方向。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        # 记录每个位置是否已经被访问过
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total
        # 右，下，左，上，符合螺旋的顺序
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                # 通过求余 循环调整方向
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order


# 法二：
# 核心思路：当遍历每一行、每一列时，都把最后一个元素留着，等到下一步再遍历。
# 这样的话，每次把矩阵剥离一圈，都对应 4 个非常规整的循环，
# 边界条件清晰不易出错。
# https://leetcode-cn.com/problems/spiral-matrix/solution/yi-chong-you-ya-de-bian-li-fang-shi-dai-ma-zheng-q/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        NROW = len(matrix)
        NCOL = len(matrix[0])
        def helper(depth):
            nrow, ncol = NROW - 2 * depth, NCOL - 2 * depth
            if nrow <= 0 or ncol <= 0: return []
            if nrow == 1: return matrix[depth][depth:depth+ncol]
            if ncol == 1: return [matrix[r][depth] for r in range(depth, depth + nrow)]

            res = []
            res += matrix[depth][depth:depth+ncol-1]
            res += [matrix[r][depth+ncol-1] for r in range(depth, depth + nrow - 1)]
            res += reversed(matrix[depth+nrow-1][depth+1:depth+ncol])
            res += [matrix[r][depth] for r in reversed(range(depth +1, depth + nrow))]
            return res + helper(depth + 1)
            
        return helper(0)




# @lc code=end

