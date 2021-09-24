#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 链表转数组，然后用108.将有序数组转换为二叉搜索树
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        def sortedArrayToBST(nums: List[int]) -> TreeNode:
            if not nums:
                return None
            # elif len(nums) == 1:
            #     return TreeNode(nums[0])
            n = len(nums)
            root = TreeNode(nums[n//2])
            root.left = sortedArrayToBST(nums[:n//2])
            root.right = sortedArrayToBST(nums[n//2+1:])
            return root
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return sortedArrayToBST(arr)
# @lc code=end

