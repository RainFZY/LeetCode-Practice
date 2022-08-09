#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# 回溯，分治
# 要返回所有可能的树，因此就把treeNode对象加入到res列表
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def subTrees(a, b):
            if a > b:
                return [None]
            res = []
            # 遍历，依次做根节点
            for i in range(a, b+1):
                # 获得所有可行的左，右子树集合
                left = subTrees(a, i-1)
                right = subTrees(i+1, b)
                # 从左子树集合中选出一棵左子树，从右子树
                # 集合中选出一棵右子树，拼接到根节点上
                for left_tree in left:
                    for right_tree in right:
                        treeNode = TreeNode(i)
                        treeNode.left = left_tree
                        treeNode.right = right_tree
                        # 每一个treeNode就代表一棵树
                        res.append(treeNode)
            return res
        # print(subTrees(1, n))
        return subTrees(1, n)
# @lc code=end

