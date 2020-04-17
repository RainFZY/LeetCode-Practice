#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
# 掌握思想即可，字符串的处理比较繁琐

# 由最高位开始，比较低一位数字，如高位大，移除，若高位小，
# 则向右移一位继续比较两个数字，直到高位大于低位则移除
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or len(num) == k:
            return '0'
        # 每次移除掉递增的最后一个
        # 否则就是移除本身了
        i = 0
        num = list(num)
        for _ in range(k):
            while i + 1 < len(num) and num[i] <= num[i + 1]:
                i += 1
            # 当前i就是递增的最后一个
            num.pop(i)
            i = 0

        c = ''.join(list(map(str, num)))
        # 去掉前导0
        return str(int(c))

# 利用栈的贪心算法
# 从左到右遍历字符串并入栈，这样栈顶存放最近的那一位（左邻居）
# 如果左邻居比当前数大，则左邻居出栈
# class Solution:
#     def removeKdigits(self, num: str, k: int) -> str:
#         numStack = []
#         count = k
#         for digit in num:
#             while count and numStack and numStack[-1] > digit:
#                 numStack.pop()
#                 count -= 1
#             numStack.append(digit)
#         finalStack = numStack[:-count] if count else numStack
#         # 奇技淫巧，去掉开始的0
#         return  "".join(finalStack).lstrip('0') or "0"

# @lc code=end

