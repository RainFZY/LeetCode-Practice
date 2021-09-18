#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 对于每一个节点，如果左/右子节点值不等于该节点，就直接赋给v1, v2，之后比较大小后return
# 如果相等，就继续递归下探去找最小的不相等的
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 第二小的值不存在的话，输出 -1
        if not root:
            return -1
        
        # 左边没有，那右边一定也没有
        if not root.left:
            return -1

        # 左/右子节点值不等于该节点
        v1 = root.left.val
        # 左/右子节点值等于该节点
        if root.val == root.left.val: 
            v1 = self.findSecondMinimumValue(root.left)
            
        v2 = root.right.val
        if root.val == root.right.val:
            v2 = self.findSecondMinimumValue(root.right)
            
        if v1 != -1 and v2 != -1:
            return min(v1, v2)
        if v1 != -1:
            return v1
        return v2		
# @lc code=end

