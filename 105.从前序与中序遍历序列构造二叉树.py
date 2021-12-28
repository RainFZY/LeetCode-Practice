#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        # 根据前序数组的第一个元素，就可以确定根节点	
        root = TreeNode(preorder[0])
        # 用preorder[0]去中序数组中查找对应的元素
        mid = inorder.index(preorder[0])
        # 递归的处理前序数组的左边部分和中序数组的左边部分
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 递归处理前序数组右边部分和中序数组右边部分
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
# @lc code=end

