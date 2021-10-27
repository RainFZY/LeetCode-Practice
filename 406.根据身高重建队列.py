#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
# greedy，较难想
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 身高按从大到小排，因为先排好高的，后面调整矮的位置时候不会影响高的的排位（第二维度的那个数）
        # 排完：[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
        # 主：x[0]倒序，次：x[1]
        people.sort(key = lambda x: [-x[0], x[1]])
        ans = []
        # k就代表了当前人应该排在的位置，即做插入操作
        for h, k in people:
            ans = ans[:k] + [[h, k]] + ans[k:]
        return ans

# @lc code=end

