#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 法一：哈希表法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        harshmap = []
        while head:
            # .count()查看数组中是否存在某个数
            if harshmap.count(head):
                return True
            else:
                harshmap.append(head)
            head = head.next
        return False


# 法二：快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
        
# @lc code=end

