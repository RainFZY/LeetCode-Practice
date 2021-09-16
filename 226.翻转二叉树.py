#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 法一：递归
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 法二：递归（变式）
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root

#         left = self.invertTree(root.left)
#         right = self.invertTree(root.right)

#         root.left = right
#         root.right = left

#         return root

# @lc code=end

