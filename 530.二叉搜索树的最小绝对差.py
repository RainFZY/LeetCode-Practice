#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 法一，BST in-order traversal, not in place
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        arr = []
        def tarversal(root):
            nonlocal arr
            if not root:
                return
            tarversal(root.left)
            arr.append(root.val)
            tarversal(root.right)
        tarversal(root)
        n = len(arr)
        for i in range(1, n):
            arr[i-1] = arr[i] - arr[i-1]
        return min(arr[:-1])
# @lc code=end

