#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.depth(root)
        return self.res

    def depth(self, root):
        if not root:
            return 0
        left_length, right_length = self.depth(root.left), self.depth(root.right)
        # 在每个节点处，都必须比较res，因为最长路径不一定包含root
        self.res = max(self.res, left_length + right_length)
        return max(left_length, right_length) + 1


        
            
# @lc code=end

