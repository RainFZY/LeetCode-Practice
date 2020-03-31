#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 法一：递归
# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         ans = []
#         self.recursion(root, ans)
#         return ans
    
#     def recursion(self, root, list):
#         if not root:
#             return
#         list.append(root.val)
#         for child in root.children:
#             self.recursion(child, list)


# 法一变式：
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res
        def helper(root):
            if root:
                res.append(root.val)
                for child in root.children:
                    helper(child)
        helper(root)
        return res


# 迭代法
# 双栈法，一个栈stack用来存给的root，另一个栈ans用来存要求的答案
# class Solution(object):
#     def preorder(self, root):
#         """
#         :type root: Node
#         :rtype: List[int]
#         """
#         if not root:
#             return []
#         stack,ans=[root],[]
#         # 树遍历迭代，判断条件都是这个
#         while stack: 
#             cur=stack.pop(-1)
#             ans.append(cur.val)
#             # 注意是extend, 逆序压入栈中
#             # 因为栈是后入先出，所以得逆一下
#             stack.extend(cur.children[::-1]) 
#         return ans

        # 变量迭代过程：
        # cur    1          3           5         6          2           4
        # ans    [1]       [1,3]       [1,3,5]   [1,3,5,6]  [1,3,5,6,2] [1,3,5,6,2,4]
        # stack  [4,2,3]   [4,2,6,5]  [4,2,6]   [4,2]      [4]

        

# @lc code=end

