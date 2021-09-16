#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 用了100、相同的树
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) \
            or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
# @lc code=end

