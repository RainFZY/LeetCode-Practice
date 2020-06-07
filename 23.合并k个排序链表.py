#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 暴力
# 把所给多个链表中的所有节点放入一个数组中，排序后加入一个链表中
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        prehead = prev = ListNode(-1)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for node in sorted(self.nodes):
            prev.next = ListNode(node)
            prev = prev.next
        return prehead.next

# 分治
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)
    
    # 同21.合并两个有序链表
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# 优先队列
# 维护当前每个链表没有被合并的元素的最前面一个
# k个链表就最多有 k个满足这样条件的元素
# 每次在这些元素里面选取 val属性最小的元素合并到答案中
# 这个答案有问题，不知为何，还有另一个版本的优先级队列
# https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/
# from queue import PriorityQueue
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         prehead = prev = ListNode(-1)
#         q = PriorityQueue()
#         for l in lists:
#             if l:
#                 q.put((l.val, l))
#         while not q.empty():
#             val, node = q.get()
#             prev.next = ListNode(val)
#             prev.next = prev
#             node = node.next
#             if node:
#                 q.put((node.val, node))
#         return prehead.next
# @lc code=end

