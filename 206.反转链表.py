#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 申请两个节点，pre和 cur，pre指向None
        prev = None
        curr = head
        # 遍历链表
        while curr:
            # 记录当前节点的下一个节点
            temp = curr.next 
            # 然后将当前节点指向pre（prev一直在curr前面，实现方向调换）
            curr.next = prev
            # pre和cur节点都前进一位
            prev = curr
            curr = temp

        return prev

# @lc code=end

