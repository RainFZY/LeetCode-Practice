#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
# BFS，较难看懂
# 0 可以 交换的位置
# e.g. 如果 0 在 1 的位置，可以交换的位置有 0, 2, 4
# moves = {
#     0: [1, 3 ],
#     1: [0, 2, 4],
#     2: [1, 5],
#     3: [0, 4],
#     4: [1, 3, 5],
#     5: [2, 4]
# }

# class Solution:
#     def slidingPuzzle(self, board: List[List[int]]) -> int:
#         used = set()
#         cnt = 0
#         s = "".join(str(c) for row in board for c in row)
#         q = [s] # ['123405']
#         while q:
#             new = []
#             for s in q:
#                 used.add(s)
#                 if s == "123450":
#                     return cnt
#                 arr = [c for c in s] # ['1', '2', '3', '4', '0', '5']
#                 # 开始移动 0
#                 zero_index = s.index('0')
#                 for move in moves[zero_index]:
#                     new_arr = arr[:]
#                     new_arr[zero_index], new_arr[move] = new_arr[move], new_arr[zero_index]
#                     new_s = "".join(new_arr) # '103425'
#                     if new_s not in used:
#                         new.append(new_s)
#             cnt += 1
#             q = new
#         return -1  

# 标准BFS模板
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 把board连起来变一维
        board = board[0] + board[1] 
        # 每个位置的0可以交换的位置
        moves = [(1, 3) , (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        # bfs队列和已访问状态记录
        q, visited = [(tuple(board), board.index(0), 0)], set()
        while q:
            # 当前状态，0的当前位置，当前步数
            state, now, step = q.pop(0)
            # 找到了
            if state == (1, 2, 3, 4, 5, 0):
                return step
            # 遍历所有可交换的位置
            for next in moves[now]:
                _state = list(state)
                # 交换位置
                _state[next], _state[now] = _state[now], _state[next]
                _state = tuple(_state)
                if _state not in visited:
                    q.append((_state, next, step + 1))
            visited.add(state)
        return -1


        
# @lc code=end

