#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Binary Search Tree, in-order traversal
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        hashMap = {} # 这题用字典比用数组更方便
        def traversal(root):
            if not root:
                return 
            traversal(root.left)
            hashMap[root.val] = hashMap.get(root.val, 0) + 1
            traversal(root.right)
        traversal(root)
        mx = max(hashMap.values()) # tricky
        res = []
        for (key, value) in hashMap.items(): # tricky
            if value == mx:
                res.append(key)
        return res
# @lc code=end

