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

# 时间复杂度：O(N^2)，其中 N 表示节点数目。
# 在深度优先搜索中每个节点会被访问一次且只会被访问一次，
# 每一次会对 path 变量进行拷贝构造，时间代价为 O(N)，
# 故时间复杂度为 O(N^2)
# 空间复杂度：O(N^2)，在最坏情况下，当二叉树中每个节点只有一个孩子节点时，
# 即整棵二叉树呈一个链状

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

