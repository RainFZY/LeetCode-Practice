#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS
class Solution:
    # 包含当前节点的path的数量
    def pathSumWithRoot(self, root: TreeNode, targetSum: int):
        if not root:
            return 0
        # 每下探到一个root都新建一个res，最后return回去
        # 相当于每一层都计算一个独立的res，然后加到上层的res中去
        res = 0
        if targetSum - root.val == 0:
            res += 1
        res += (self.pathSumWithRoot(root.left, targetSum-root.val) + \
            self.pathSumWithRoot(root.right, targetSum-root.val))
        return res

    # 所有path = 不包含当前节点的path + 包含当前节点的path
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) \
            + self.pathSumWithRoot(root, targetSum) 

# 嵌入式写法，同上
class Solution:
    # 所有path = 不包含当前节点的path + 包含当前节点的path
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        def dfs(root: TreeNode, targetSum: int):
            if not root:
                return 0
            cnt = 0
            if targetSum - root.val == 0:
                cnt += 1
            cnt += (dfs(root.left, targetSum-root.val) + \
                dfs(root.right, targetSum-root.val))
            return cnt
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) \
            + dfs(root, targetSum) 


# DFS，较难懂
# https://leetcode-cn.com/problems/path-sum-iii/solution/437zhi-xu-yi-ci-di-gui-wu-xing-dai-ma-yong-lie-bia/
# 计算每一步中，sum在数组sumlist中出现的次数，然后与每一轮递归的结果相加
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int):
        res = 0
        def dfs(root, sumlist):
            if not root:
                return 0
            # 更新为，上一层的所有sumlist值加上当前节点的值，
            # 因此下探时不会重复计算之前的
            sumlist = [num + root.val for num in sumlist]
            sumlist.append(root.val)
            cnt = sumlist.count(targetSum)
            return cnt + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        res = dfs(root, [])
        return res
            



# @lc code=end

