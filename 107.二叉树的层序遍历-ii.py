#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 同102 二叉树的层序遍历，只不过res反了一下
# DFS
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        def dfs(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        dfs(root, 0)
        res.reverse()
        return res

# BFS
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        while cur_level:
            next_level = []
            temp = []
            for node in cur_level:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
            res.append(temp)
        res.reverse()
        return res
# @lc code=end

