#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 对二叉树做深度优先遍历DFS，递归过程中：
# 终止条件：当DFS越过叶子节点时，返回高度0；
# 返回值：
# 从底至顶，返回以每个节点root为根节点的子树最大高度(左右子树中最大的高度值加1max(left,right) + 1)；
# 当我们发现有一例 左/右子树高度差 ＞ 1 的情况时，代表此树不是平衡树，返回-1，此时就会终止
# 当发现不是平衡树时，后面的高度计算都没有意义了，因此一路返回-1，避免后续多余计算。
# 最差情况是对树做一遍完整DFS，时间复杂度为 O(N)

# 整个程序执行时会先按DFS到底，然后一级一级自底而上返回该节点的depth或-1（提前终止）

# 法一：
# 先会一探到底，若发现非平衡二叉树，返回-1，之后往上的节点就都是-1（非平衡）
# 这样就避免了重复计算
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 若root的深度不等于-1，则返回true，为平衡二叉树
        return self.depth(root) != -1

    # 若是平衡二叉树，返回子树最大高度
    # 若不是，返回-1
    def depth(self, root):
        if root == None:
            # 这里只要返回一个不是-1的都行
            return 0
        leftHeight = self.depth(root.left)
        rightHeight = self.depth(root.right)
        if leftHeight == -1 or rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1

        return max(leftHeight, rightHeight) + 1 

    # def depth(self, root):
        # if abs(left - right) <= 1:
        #     return max(left, right) + 1
        # else:
        #     return -1
        # 简化以上写法

# 法二：更简洁，但存在重复计算，time complexity高
class Solution:
    def depth(self, root: TreeNode) -> int:
        if root == None:
            return -1
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        # 递归，自顶向下的过程中，每一个父节点满足条件且两个子节点也满足条件，
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)




        
# @lc code=end

