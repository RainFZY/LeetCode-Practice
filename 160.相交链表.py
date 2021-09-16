#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            if not cur1:
                cur1 = headB
            else:
                cur1 = cur1.next
            if not cur2:
                cur2 = headA
            else:
                cur2 = cur2.next
        return cur1
            
        
# @lc code=end

