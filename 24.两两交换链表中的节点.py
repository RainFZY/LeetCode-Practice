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
# 每一次while循环的效果是cur之后的两个节点交换位置，结束后cur移动两位
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 哨兵节点
        pre = ListNode()
        pre.next = head
        cur = pre # pre是head前面的节点
        while cur.next != None and cur.next.next != None:
            # 两两交换其中相邻的节点
            start = cur.next
            end = cur.next.next
            cur.next = end
            start.next = end.next
            end.next = start
            # cur往前移动两位
            cur = start
        
        return pre.next

# 法二：递归，很难想到
                


# @lc code=end

