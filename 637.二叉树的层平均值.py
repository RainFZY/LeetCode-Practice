#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 类似102 二叉树的层序遍历
# BFS
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            cur_sum = 0 # 记录当前层的和
            next_level = []
            for node in queue:
                cur_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(cur_sum / len(queue))
            queue = next_level
        return res

# DFS
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        for i in range(len(res)):
            temp = res[i].copy()
            res[i] = sum(temp)/len(temp)
        return res
            
# @lc code=end

