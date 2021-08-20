#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先将l1和l2头节点的值加起来赋值给新链表的头节点
        head = ListNode(l1.val + l2.val)
        cur = head
        # 遍历两个链表，只要有一个链表还没有遍历到末尾，就继续遍历
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            # 每次遍历生成一个当前节点cur的下一个节点，
            # 其值为两链表对应节点的和再加上当前节点cur产生的进位
            cur.next = ListNode(l1.val + l2.val + cur.val // 10)
            # 更新进位后的当前节点cur的值
            cur.val = cur.val % 10
            cur = cur.next
        # 循环结束后，因为首位可能产生进位，因此如果cur.val是两位数的话，新增一个节点
        if cur.val >= 10:
            cur.next = ListNode(cur.val // 10)
            cur.val = cur.val % 10
        # 返回头节点
        return head
# @lc code=end

