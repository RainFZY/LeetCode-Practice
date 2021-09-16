#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # 说明此路不行
        if not root:
            return False
        # 下探最下面的节点，判断是否减到了0
        if not root.left and not root.right and sum - root.val == 0:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# @lc code=end

