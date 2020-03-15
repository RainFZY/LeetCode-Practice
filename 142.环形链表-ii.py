#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 法一：哈希表法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        harshMap = []
        while head:
            if harshMap.count(head):
                return head
            harshMap.append(head)
            head = head.next
        return None


# 法二：双指针，技巧性较强，这道题下需要数学证明，推荐哈希表法

# @lc code=end

