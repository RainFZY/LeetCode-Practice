#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 用字典存储中间量，优化递归
class Solution:
    global longestDict
    longestDict = {}
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        left_longest, right_longest = 0, 0
        if root.left and root.left.val == root.val:
            left_longest = self.longest(root.left) + 1
        if root.right and root.right.val == root.val:
            right_longest = self.longest(root.right) + 1
        # 该节点最长：left_longest + right_longest，但也可能left和right节点存在更长
        # 所以取max
        return max(left_longest + right_longest, self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right)) 
    # 包含该节点的，单边最长（不能左右都有，拐弯）
    def longest(self, root):
        if not root:
            return 0
        if longestDict.get(root):
            return longestDict[root]
        left_longest, right_longest = 0, 0
        if root.left and root.left.val == root.val:
            left_longest = self.longest(root.left) + 1
        if root.right and root.right.val == root.val:
            right_longest = self.longest(root.right) + 1
        longestDict[root] = max(left_longest, right_longest)
        return max(left_longest, right_longest)

# 优化版，但是很难想
class Solution:
    def longestUnivaluePath(self, root):
        self.longestPath = 0
        self.longest(root)
        return self.longestPath
    # 这个函数做了两件事，一是在每个结点处比较并更新self.longestPath
    # 二是return当前节点处的单边最长（不能左右都有，拐弯），用于自身递归
    def longest(self, root):
        if not root:
            return 0
        left_longest, right_longest = 0, 0
        path_of_left = self.longest(root.left)
        path_of_right = self.longest(root.right)
        if root.left and root.left.val == root.val:
            left_longest = path_of_left + 1
        if root.right and root.right.val == root.val:
            right_longest = path_of_right + 1
        curLongest = left_longest + right_longest 
        # 比较并更新self.longestPath
        if curLongest > self.longestPath:
            self.longestPath = curLongest 
        return max(left_longest, right_longest)

# @lc code=end

