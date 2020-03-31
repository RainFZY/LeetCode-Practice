#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 法一，递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
        helper(root)
        return res

# 法二，迭代，左右中
# 思路是中右左，再倒过来
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         stack = [root]
#         if not root:
#             return res
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
#             if node.left:
#                 stack.append(node.left)
#             if node.right:
#                 stack.append(node.right)       
#         res[:] = res[::-1]
#         return res
        
# @lc code=end

