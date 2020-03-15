#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 法一：中序遍历提取树中的所有节点的值，放入一个数组中，验证这个数组是否是升序数组
# 但这个方法把所有节点都保存了一遍，内存利用率较高
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         order = self.getOrder(root)
#         # set()的作用是把数组中的元素提取出来放到一个集合中，
#         # 这样重复的元素只被提取一次，有判重作用
#         return order == list(sorted(set(order)))
    
#     def getOrder(self, root):
#         if root == None:
#             return []
#         return self.getOrder(root.left) + [root.val] + self.getOrder(root.right)

# 法二：递归
class Solution:
    # 这里用了一个小技巧，给min和max分别赋了一个无限大的初值
    def isValidBST(self, root: TreeNode, min = float('-inf'), max = float('inf')) -> bool:

        if root == None:
            return True
        if root.val <= min or root.val >= max:
            return False
        # 递归过程，向下检测左右子树，传入新的最大值最小值
        return self.isValidBST(root.left, min, root.val) and \
        self.isValidBST(root.right, root.val, max)

    


# @lc code=end

