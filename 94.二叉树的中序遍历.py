#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 法一，递归
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         return self.helper(root, res)

#     def helper(self, root, res):
#         if not root:
#             return []
#         self.helper(root.left, res)
#         res.append(root.val) # 别漏掉.val
#         self.helper(root.right, res)
#         return res

# 法一变式
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val) # 别漏掉.val
                helper(root.right)
        helper(root)
        return res

# 法二，迭代，利用栈
# 因为左下角最小，先left探到底，全部加到stack
# 再利用stack后入先出，把right也加进去
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         stack = []
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             # 后入先出 --> stack
#             root = stack.pop()
#             res.append(root.val) # 别漏掉.val
#             root = root.right
#         return res



# @lc code=end

