#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归，跟112先比增加了temp数组存储路径
# 经典递归模板
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def recursion(root, sum, temp):
            if not root:
                return 
            if not root.left and not root.right and sum - root.val == 0:
                temp += [root.val]
                res.append(temp)
            recursion(root.left, sum - root.val, temp + [root.val])
            recursion(root.right, sum - root.val, temp + [root.val])
        recursion(root, sum, [])
        return res


# @lc code=end

