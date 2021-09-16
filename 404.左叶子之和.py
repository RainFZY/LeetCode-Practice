#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 法一，DFS，自己写的
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                self.res += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res

# 法二
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 寻找左边的叶子节点
        if self.isLeaf(root.left):
            left = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        # 和 = 左边的 + 右边的
        return left + self.sumOfLeftLeaves(root.right)

    # 判断节点是否为叶子节点
    def isLeaf(self, root):
        if not root:
            return False
        return  not root.left and not root.right

# @lc code=end

