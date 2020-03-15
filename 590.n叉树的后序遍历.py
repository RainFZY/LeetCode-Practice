#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 法一：递归法
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         ans = []
#         self.recursion(root, ans)
#         ans.append(root.val)
#         return ans

#     def recursion(self, root, list):
#         if not root:
#             return 
#         for child in root.children:
#             self.recursion(child, list)
#             list.append(child.val)

# 法一变式
# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         res = []
#         if not root:
#             return res
#         def helper(root):
#             if root:
#                 for child in root.children:
#                     helper(child)
#                 res.append(root.val)
#         helper(root)
#         return res


# 法二：迭代法
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            current = stack.pop()
            ans.append(current.val)
            stack.extend(current.children[:])
        # 后序遍历的迭代法的思路一般都是按倒着排最后再倒过来
        ans.reverse()
        
        return ans
  
        
# @lc code=end

