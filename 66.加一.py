#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start

# 法一
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         n = len(digits)
#         num = 0
#         for i in range(n):
#             num += digits[i] * pow(10, (n-i-1))
#         num += 1
#         num = str(num)
#         # digits = []
#         print(len(num))
#         for i in range(len(num)):
#             digits.append(int(num[i]))
#         return digits

# 法二：巧妙倒序解法，很难想到
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
        digits = [1] + digits
        return digits

# @lc code=end

