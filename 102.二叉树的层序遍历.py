#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        # 维护一个队列，记录已经遍历到但还没有扩展的顶点
        cur_level = [root]
        # while循环每执行一次，都是cur_level和next_level交替的时候，
        # 也就是探到下一层的时候
        while cur_level:
            next_level = []
            temp = []
            # 遍历这一层中的节点
            for node in cur_level:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(temp)
            # 更新队列
            cur_level = next_level
        return res

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

# 复习，dfs
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        def dfs(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level+1)
            if root.right:
                dfs(root.right, level+1)
        dfs(root, 0)
        return res

# 复习，BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            next_level = []
            temp = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(temp)
            queue = next_level
        return res



# @lc code=end

