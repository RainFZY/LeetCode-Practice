#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 迭代法
# 每一次while循环的效果是temp之后的两个节点交换位置，结束后temp移动两位
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode()
        pre.next = head
        temp = pre # pre是head前面的节点
        while temp.next != None and temp.next.next != None:
            start = temp.next
            end = temp.next.next
            temp.next = end
            start.next = end.next
            end.next = start
            temp = start
        
        return pre.next

# 法二：递归，很难想到
                


# @lc code=end

