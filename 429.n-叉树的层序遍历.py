#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 法一，递归
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def helper(root, level):
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            for child in root.children:
                helper(child, level + 1)
        if root:
            helper(root, 0)
        return res
# @lc code=end

