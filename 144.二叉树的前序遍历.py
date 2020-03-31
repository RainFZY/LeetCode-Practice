#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 法一，递归
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                res.append(root.val) # 别漏掉.val
                helper(root.left)
                helper(root.right)
        helper(root)
        return res

# 法二，迭代，中左右
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
#             if node.right:
#                 stack.append(node.right) # 由于栈是先入后出，所以先加右
#             if node.left:
#                 stack.append(node.left)
#         return res

# @lc code=end

