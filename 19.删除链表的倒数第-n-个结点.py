#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/san-chong-fang-fa-shan-chu-dao-shu-di-nge-jie-dian/
# 法一，暴力法，两次遍历
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = ListNode(0, head) # 哨兵节点，prev.next = head
        # 获取链表长度
        cur, len = prev, 0
        while cur.next:
            cur = cur.next
            len += 1
        # 找到倒数第N个节点的前面一个节点
        cur = prev
        for _ in range(len-n):
            cur = cur.next
        # 删除节点，并重新连接
        cur.next = cur.next.next
        return prev.next

# 法二，双指针
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = ListNode(0, head) # 哨兵节点，prev.next = head
        left, right = prev, prev
        # 快指针先走n步
        for _ in range(n):
            right = right.next
        # 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while right and right.next:
            left, right = left.next, right.next
        # 删除节点，并重新连接
        left.next = left.next.next
        return prev.next


# @lc code=end

