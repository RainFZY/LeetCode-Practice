#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right、

# BST中序遍历 + 双指针搜索
# O(n)时间复杂度，0(n)空间复杂度，空间还可以优化
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        arr = []
        def traversal(root):
            nonlocal arr
            if not root:
                return
            traversal(root.left)
            arr.append(root.val)
            traversal(root.right)
        traversal(root)
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] == k:
                return True
            elif arr[left] + arr[right] > k:
                right -= 1
            else:
                left += 1
        return False

# 非递归写法的in-order traversal --> stack
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def traversal(root):
            res = []
            stack = []
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                # 后入先出 --> stack
                root = stack.pop()
                res.append(root.val)
                root = root.right
            return res
        arr = traversal(root)
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] == k:
                return True
            elif arr[left] + arr[right] > k:
                right -= 1
            else:
                left += 1
        return False
# @lc code=end

