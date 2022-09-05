#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# 二叉树层序遍历解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:  # 遍历每一层
            length = len(queue)
            tail = None # 每一层维护一个尾节点
            for i in range(length): # 遍历当前层
                curnode = queue.pop(0)
                if tail:
                    tail.next = curnode # 让尾节点指向当前节点
                tail = curnode # 让当前节点成为尾节点
                if curnode.left : queue.append(curnode.left)
                if curnode.right: queue.append(curnode.right)
        return root


# 链表解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return
        cur = root
        while cur:
            # 遍历当前层的时候，为了方便操作在下一
            # 层前面添加一个哑结点（注意这里是访问
            # 当前层的节点，然后把下一层的节点串起来）
            dhead = Node(None)
            # pre表示访下一层节点的前一个节点
            pre = dhead
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dhead.next
        return root
        
# @lc code=end

