#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 法一，递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        
        if(l1.val < l2.val):
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

# 法二，迭代
# 动画可以看https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode/
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 哨兵节点，-1是它的value，可以换任意的
        prehead = ListNode(-1)
        # prev初始在prehead上，之后每次指向最新的节点并移动过去
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            # prev自我更新，移动到最新的位置上
            prev = prev.next
        # 哪个还有多就把哪个补上
        prev.next = l1 if l1 else l2

        # 最后去掉哨兵节点，返回它之后的
        return prehead.next

        
# @lc code=end

