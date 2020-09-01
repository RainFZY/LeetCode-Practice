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

# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 申请两个节点，pre和 cur，pre指向None
        # prev一直在curr前面，用于实现方向调换
        prev = None
        curr = head
        # 遍历链表
        while curr:
            # 记录当前节点的下一个节点
            nextTemp = curr.next 
            # 然后将当前节点指向pre，实现方向调换
            curr.next = prev
            # pre前进一位
            prev = curr
            # cur前进一位
            curr = nextTemp

        return prev

# 递归
class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		# 递归终止条件是当前为空，或者下一个节点为空
		if(head==None or head.next==None):
			return head
		# 这里的cur就是最后一个节点
		cur = self.reverseList(head.next)
		# 这里请配合动画演示理解
		# 如果链表是 1->2->3->4->5，那么此时的cur就是5
		# 而head是4，head的下一个是5，下下一个是空
		# 所以head.next.next 就是5->4
		head.next.next = head
		# 防止链表循环，需要将head.next设置为空
		head.next = None
		# 每层递归函数都返回cur，也就是最后一个节点
		return cur


# @lc code=end

