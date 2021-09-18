#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DP
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root):
            if not root:
                return 0, 0
            left, right = dp(root.left), dp(root.right)
            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点, 则取左右子树中最大的值
            v2 = max(left) + max(right)
            return v1, v2
        
        return max(dp(root))

# 最简版
# ls表示偷左子树能带来的最大收益，ln表示不偷左子树能带来的最大收益，rs、rn同理
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(root):
            if not root:
                return 0, 0
            ls, ln = dp(root.left)
            rs, rn = dp(root.right)
            return root.val + ln + rn, max(ls, ln) + max(rs, rn)
        
        return max(dp(root))


# @lc code=end

