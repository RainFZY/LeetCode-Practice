#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 我的写法，先序遍历 preoder traversal，先都存进去，最后再比较
# 比较 中左右 是否等于 中右左
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        leftList, rightList = [], []
        def dfs_left(root):
            if not root:
                leftList.append('None')
                return
            leftList.append(root.val)
            dfs_left(root.left)
            dfs_left(root.right)
        def dfs_right(root):
            if not root:
                rightList.append('None')
                return
            rightList.append(root.val)
            dfs_right(root.right)
            dfs_right(root.left)

        dfs_left(root)
        dfs_right(root)
        # print(leftList, rightList)
        return leftList == rightList

# 先序遍历，随时比较
# （父亲 左孩子 右孩子）和与其对称的先序遍历（父亲 右孩子 左孩子），比对结果是否相同
class Solution:
    def isSymmetric1(self, root: TreeNode) -> bool:
        def search(left, right):
            if left is None and right is None:
                return True
            elif left is None and right is not None:
                return False
            elif right is None and left is not None:
                return False
            else:
                if left.val != right.val:
                    return False
                else:
                    return search(left.left, right.right) and search(left.right, right.left)
        return search(root, root)
# @lc code=end

