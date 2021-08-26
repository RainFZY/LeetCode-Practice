#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
# 回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backTrack(start = 1, temp = []):
            # 剪枝，不剪也行，但是影响runtime
            if start + k > n + len(temp) + 1:
                return 
            # terminator
            if len(temp) == k:
                # 注意一定要加[:]
                res.append(temp[:])
                return

            for i in range(start, n + 1):
                # process
                temp.append(i)
                # drill down
                backTrack(i + 1, temp)
                # reverse state
                temp.pop()
        backTrack()
        return res


# 二刷
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backTrack(start=1, temp=[]):
            if len(temp) == k:
                res.append(temp[:])
                return
            for i in range(start, n+1):
                temp.append(i)
                backTrack(i+1, temp)
                temp.pop()
        backTrack(1, [])
        return res

# 三刷
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backTrack(start, temp):
            if len(temp) == k:
                res.append(temp[:]) # 这一行漏了
                return
            for i in range(start, n+1):
                temp.append(i)
                backTrack(i+1, temp) # 这里写成了start+1
                temp.pop()
        backTrack(1, [])
        return res
# @lc code=end

