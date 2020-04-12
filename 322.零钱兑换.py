#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
# 法一：动态规划（自底向上）
# 到amount的最少数量 = 到(amount - 某个coin值)的最少数量 + 1（那个coin）
# 用一个数组存储0 - amount每个值对应的最少数量，若没法凑出则是初始化的amount + 1
# DP方程：f(n) = min(f(n - k) for k in [1, 2, 5]) + 1 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount + 1] * (amount + 1)
        res[0] = 0
        for x in range(1, amount + 1):
            for coin in coins:
                if coin <= x:
                    res[x] = min(res[x] , res[x - coin] + 1)
        return res[amount] if res[amount] < amount + 1 else -1


# 法二：递归（自顶向下），用LRU Cache
# import functools
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @functools.lru_cache(amount) # 及时释放缓存，相当于递归树的剪枝，避免重复计算
#         def dp(amount):
#             # terminator
#             if amount < 0: return -1
#             if amount == 0: return 0
#             # min = float('inf')
#             min = amount + 1 # 最大边界（coin全是1）
#             for coin in coins:
#                 # key step，drill down
#                 temp = dp(amount - coin)
#                 if temp >= 0 and temp + 1 <= min:
#                     min = temp + 1
#             return min if min < amount + 1 else -1
            
#         return dp(amount) 


# 法二：递归，用哈希表存储中间结果
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         hashMap = {}
#         def dp(amount):
#             # terminator
#             if amount < 0: return -1
#             if amount == 0: return 0
#             # min = float('inf')
#             if hashMap.get(amount):
#                 return hashMap[amount]
#             else:
#                 min = amount + 1 # 最大边界（coin全是1）
#                 for coin in coins:
#                     # key step，drill down
#                     temp = dp(amount - coin)
#                     if temp >= 0 and temp + 1 <= min:
#                         min = temp + 1
#                 hashMap[amount] = min if min < amount + 1 else -1
#                 return hashMap[amount]
            
#         return dp(amount) 
        
# @lc code=end

