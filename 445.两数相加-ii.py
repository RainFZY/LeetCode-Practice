#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 法一，因为要从链表尾部先开始相加，后入先出，想到用栈
# 对于逆序处理应该首先想到栈
from typing import List
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1, cur2 = l1, l2
        stack1, stack2 = [], []
        # 把两条链表节点的值分别存入两个stack
        while cur1:
            stack1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            stack2.append(cur2.val)
            cur2 = cur2.next
        carry = 0 # 是否进位
        res = None
        # 把节点依次从stack中取出，因为后入先出，所以先计算低位的加法
        while stack1 or stack2 or carry:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            sum = a + b + carry
            carry = sum // 10
            sum %= 10
            # 下面两句需要好好理解下
            # 新建一个值为sum的节点，并指向res
            # （res最开始为None，相当于最尾部的节点指向None）
            # 之后更新res为刚建的节点，下一个loop中新建的节点会指向之前的节点
            # 成功串起来
            curNode = ListNode(sum, res)
            res = curNode
        return res

# 法二，反转链表，单独写一个反转函数


# @lc code=end

