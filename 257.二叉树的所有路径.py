#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root, path):
            if not root.left and not root.right:
                path += str(root.val)
                res.append(path)
            if root.left:
                dfs(root.left, path+str(root.val)+"->")
            if root.right:
                dfs(root.right, path+str(root.val)+"->")
            
            return res
        return dfs(root, "")
# @lc code=end

