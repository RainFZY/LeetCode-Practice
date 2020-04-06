#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
# 法一：动态规划（自底向上）
# 到amount的最少数量 = 到(amount - 某个coin值)的最少数量 + 1（那个coin）
# 用一个数组存储0 - amount每个值对应的最少数量
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount + 1] * (amount + 1)
        res[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                res[x] = min(res[x] , res[x - coin] + 1)
        return res[amount] if res[amount] < amount + 1 else -1


# 法二：动态规划（自顶向下）
# import functools
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @functools.lru_cache(amount) # 及时释放缓存
#         def dp(amount):
#             if amount < 0: return -1
#             if amount == 0: return 0
#             # min = float('inf')
#             min = amount + 1 # 最大边界（coin全是1）
#             for coin in coins:
#                 # key step
#                 temp = dp(amount - coin)
#                 if temp >= 0 and temp + 1 <= min:
#                     min = temp + 1
#             return min if min < amount + 1 else -1
            
#         return dp(amount) 

        
# @lc code=end

