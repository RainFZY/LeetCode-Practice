#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        if root == p or root == q:
            return root
        # 找左子树中是否存在pq节点，若存在则返回该节点，不存在则返回None
        left = self.lowestCommonAncestor(root.left, p, q) 
        # 找右子树中是否存在pq节点
        right = self.lowestCommonAncestor(root.right, p, q) 
        # 自顶而下搜索过程中，第一次出现左右各有一个pq的必然是最近公共祖先
        if left and right:
            return root
        # 两个节点都在右边
        if left == None:
            return right
        if right == None:
            return left
        
# @lc code=end

