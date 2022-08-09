#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉搜索树中序遍历
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.cnt, self.res = 0, 0
        def helper(root):
            # nonlocal cnt, res
            if not root:
                return 
            helper(root.left)
            # 对于每个root，先往left一探到底，到最小值
            self.cnt += 1 # 必须在left和right中间加
            if self.cnt == k:
                self.res = root.val
                return
            helper(root.right)

        helper(root)
        return self.res
        
# @lc code=end

