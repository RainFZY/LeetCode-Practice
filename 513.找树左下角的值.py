#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 类似102 二叉树的层序遍历
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return root.val
        queue = [root]
        res = 0
        while queue:
            next_level = []
            temp = []
            for node in queue:
                temp.append(node.val)
                # 因为要找左下角，因此先右后左，这样最后一个就是左下角节点
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)
            res = temp[-1]
            queue = next_level
        return res


# DFS
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = []
        def dfs(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        dfs(root,0)
        return res[-1][0]


# @lc code=end

