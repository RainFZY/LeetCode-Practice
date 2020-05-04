#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
# 有序字典，如果不用有序字典的话得手写双向链表实现
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = OrderedDict()

    def get(self, key):
        if key not in self.dict:
            return - 1
        
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key, value):
        if key in self.dict:
            self.dict.move_to_end(key)
        self.dict[key] = value
        if len(self.dict) > self.capacity:
            self.dict.popitem(last = False)

# LRUCache 对象会以如下语句构造和调用:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end

