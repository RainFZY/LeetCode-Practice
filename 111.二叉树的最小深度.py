#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 跟104最大深度的做法不同，最小深度条件的判断更苛刻一些
# 因为一边有节点一边是0(没有节点)的情况不能满足min()+1的公式，需要单独列出考虑
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth and right_depth:
            return min(left_depth, right_depth) + 1
        # 只有一边有节点，另一边是null，对应depth为0
        elif left_depth or right_depth:
            return left_depth + right_depth + 1
        else:
            return 1

# @lc code=end

