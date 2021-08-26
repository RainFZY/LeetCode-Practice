#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
# https://leetcode-cn.com/problems/zigzag-conversion/solution/zzi-xing-bian-huan-by-jyd/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        # 拆分每一行
        res = ["" for _ in range(numRows)] # ['', '', '']
        # i 表示当前行，flag表示当前遍历顺序（上到下或下到上）
        i, flag = 0, -1
        for char in s:
            res[i] += char
            # 在达到 Z 字形转折点时，执行反向
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        res = "".join(res) # 整型数组转字符串
        return res
# @lc code=end

