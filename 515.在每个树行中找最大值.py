#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归，DFS
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        temp = []
        def recursion(root, level):
            if not root:
                return
            if len(temp) == level:
                temp.append([])
            temp[level].append(root.val)
            if root.left:
                recursion(root.left, level + 1)
            if root.right:
                recursion(root.right, level + 1)
        recursion(root, 0)
        # print(temp)
        ans = []
        for i in range(len(temp)):
            ans.append(max(temp[i]))
        return ans
# @lc code=end

