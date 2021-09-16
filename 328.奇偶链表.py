#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 自己写的，有点屎
# odd和even分别遍历，因为odd遍历时候就会改变原head，所以deepcopy一份给even
import copy
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        head2 = copy.deepcopy(head)
        prev = head2.next
        odd, even = head, prev
        while odd.next and odd.next.next:
            odd.next = odd.next.next
            odd = odd.next
        while even and even.next and even.next.next:
            even.next = even.next.next
            even = even.next
        if even:
            even.next = None
        odd.next = prev
        return head

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        prev = head.next
        odd, even = head, prev
        # 条件必须这么写
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        # 最后要让odd的尾串even的头，而even已经遍历到最后了
        # 所以要设prev作为even的头节点
        odd.next = prev
        return head
# @lc code=end

