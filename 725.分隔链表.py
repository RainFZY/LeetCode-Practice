#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 这题很麻烦
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        total_len = 0
        cur = head
        while cur:
            total_len += 1
            cur = cur.next
        len = total_len // k # 每段的基础长度
        m = total_len % k # 前m个划分要多出一个节点
        res = []
        cur = head
        for _ in range(k):
            res.append(cur) # 先都放进去，再划分
            # print(res)
            size = len + (1 if m > 0 else 0) # 算出每段的长度
            if cur:
                for _ in range(size-1):
                    cur = cur.next
                m -= 1
                # 把后面一段截掉，后面一段需在后面继续划分
                temp = cur.next
                cur.next = None
                cur = temp
        return res

# @lc code=end

