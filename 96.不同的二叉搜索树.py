#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
# DP
# G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数
# 令 f(i) 为以 i 为根的二叉搜索树的个数
# G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
# 当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，则
# f(i) = G(i-1)*G(n-i)
# 综合以上公式，消掉f(n)
# G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n+1)
        G[0] = 1 # 空树
        G[1] = 1 # 只有跟
        for i in range(2, n+1):
            # 遍历j，依次做根节点
            for j in range(1, n+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]

# 95回溯修改，超时
# class Solution:
#     def numTrees(self, n: int) -> int:
#         def subTrees(a, b):
#             if a > b:
#                 return [None]
#             res = []
#             # 遍历，依次做根节点
#             for i in range(a, b+1):
#                 # 获得所有可行的左，右子树集合
#                 left = subTrees(a, i-1)
#                 right = subTrees(i+1, b)
#                 # 从左子树集合中选出一棵左子树，从右子树
#                 # 集合中选出一棵右子树，拼接到根节点上
#                 for left_tree in left:
#                     for right_tree in right:
#                         treeNode = TreeNode(i)
#                         treeNode.left = left_tree
#                         treeNode.right = right_tree
#                         res.append(treeNode)
#             return res
#         return len(subTrees(1, n))
# @lc code=end

