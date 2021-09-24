#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉搜索树中序遍历
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        def traversal(root):
            nonlocal cur_sum
            if not root:
                return
            traversal(root.right)
            root.val, cur_sum = root.val + cur_sum, root.val + cur_sum
            traversal(root.left)
        traversal(root)
        return root

# @lc code=end

