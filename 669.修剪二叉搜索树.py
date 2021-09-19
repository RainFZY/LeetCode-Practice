#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 实例二，输入每个节点的返回值
# trimBST(node(1)): node(1)
# trimBST(node(2)): node(2)
# trimBST(node(0)):  node(2)
# trimBST(node(4)): Null

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        # 符合要求，继续连接左右子节点
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
        # 不符合要求，返回可能符合要求的一边
        elif root.val < low:
            return self.trimBST(root.right, low, high)
        else:
            return self.trimBST(root.left, low, high)

# @lc code=end

