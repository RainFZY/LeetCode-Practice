#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 法一，额外O(n)空间
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        cur = head
        temp = []
        while cur:
            temp.append(cur.val)
            cur = cur.next
        return temp == temp[::-1]

# 法二，反转一半的链表
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 反转链表函数
        def reverseList(head):
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = reverseList(slow) # 反转后一半链表
        # 这时slow在函数中已经变换了位置，换到了最后一个节点
        cur = head
        while cur and slow:
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
        return True


# @lc code=end

