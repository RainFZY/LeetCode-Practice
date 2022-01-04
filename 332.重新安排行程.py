#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

# @lc code=start

# 回溯
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for [start, end] in tickets:
            tickets_dict[start].append(end)
        res = ["JFK"]
        def backtrack(cur_start):
            # 结束条件
            if len(res) == len(tickets) + 1:
                return True
            # 按字母排序
            tickets_dict[cur_start].sort()
            for _ in tickets_dict[cur_start]:
                # 取出并选择当前节点
                cur_end = tickets_dict[cur_start].pop(0) 
                res.append(cur_end)
                # 回溯，满足结束条件则一直return True
                if backtrack(cur_end):
                    return True
                # 撤销选择并恢复
                res.pop()
                tickets_dict[cur_start].append(cur_end)
            return False
        
        backtrack("JFK")
        return res


# res, temp的版本
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets_dict = defaultdict(list)
        for [start, end] in tickets:
            tickets_dict[start].append(end)
        self.res = []
        def backtrack(cur_start, temp):
            # 结束条件
            if len(temp) == len(tickets) + 1:
                self.res = temp.copy()
                return True
            # 按字母排序
            tickets_dict[cur_start].sort()
            for _ in tickets_dict[cur_start]:
                # 取出并选择当前节点
                cur_end = tickets_dict[cur_start].pop(0) 
                temp.append(cur_end)
                # 回溯，满足结束条件则一直return True
                if backtrack(cur_end, temp):
                    return True
                # 撤销选择并恢复
                temp.pop()
                tickets_dict[cur_start].append(cur_end)
            return False

        backtrack("JFK", ["JFK"])
        return self.res


# @lc code=end

