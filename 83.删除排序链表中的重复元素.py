#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 法一：迭代
# 用一个current表示当前遍历到的节点
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while(current and current.next):
            # 遇到相同的，改变链表的连接
            if current.val == current.next.val:
                current.next = current.next.next
            # 没毛病，正常继续迭代
            else:
                current = current.next
        
        return head


# 法二：递归
# 思路：如果当前节点和下一个节点的值相同，则返回第二个节点
# 在每个递归中将下一个递归结果连接到当前节点
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         if head:
#             head.next = self.deleteDuplicates(head.next)
#             if head.next and head.val == head.next.val:
#                 return head.next  
#             else:
#                 return head


           
        

# @lc code=end

