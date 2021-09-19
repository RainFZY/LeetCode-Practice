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
        cnt, res = 0, 0
        def helper(root):
            nonlocal cnt, res
            if not root:
                return 
            helper(root.left)
            cnt += 1 # 必须在left和right中间加
            if cnt == k:
                res = root.val
                return
            helper(root.right)
        print(cnt)
        helper(root)
        return res
        
# @lc code=end

