#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root:
#             return []
#         res = []
#         cur_level = [root]
#         while cur_level:
#             next_level = []
#             temp = []
#             for node in cur_level:
#                 temp.append(node.val)
#                 if node.left:
#                     next_level.append(node.left)
#                 if node.right:
#                     next_level.append(node.right)
#             res.append(temp)
#             cur_level = next_level
#         return res

# DFS，递归：
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        def recursion(root, level):
            if not root:
                return 
            if len(res) == level:
                res.append([])
            # 核心的一行
            res[level].append(root.val)
            if root.left:
                recursion(root.left, level + 1)
            if root.right:
                recursion(root.right, level + 1)

        recursion(root, 0)
        return res
# @lc code=end

