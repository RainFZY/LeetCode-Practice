#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 算法
# 从根节点开始遍历树，搜索最近公共祖先点
# 如果节点 p 和节点 q 都在右子树上，那么以右孩子为根节点继续 1 的操作
# 如果节点 p 和节点 q 都在左子树上，那么以左孩子为根节点继续 1 的操作
# 如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 p 和节点 q 的 LCA 了


# 法一：递归
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root.val > p.val and root.val > q.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         if root.val < p.val and root.val < q.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         return root

# 法二：迭代
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root is not None:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:    
                return root
# @lc code=end

