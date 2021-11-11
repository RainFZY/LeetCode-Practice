#
# @lc app=leetcode.cn id=605 lang=python3
#
#  
#

# @lc code=start

# 贪心，从头到尾，碰到能种的位置就种
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0] # key line，破解边界条件
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count = count + 1
            if count >= n:
                return True
        return False


# 跳格子解法
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, length = 0, len(flowerbed)
        while i < length and n>0:
            #当遍历到index遇到1时，说明这个位置有花，
            # 那必然从index+2的位置才有可能种花，因此当碰到1时直接跳过下一格。
            if flowerbed[i]==1:
                i += 2
            # 当遍历到index遇到0时，由于每次碰到1都是跳两格，因此前一格必定是0，
            # 此时只需要判断下一格是不是1即可得出index这一格能不能种花
            elif flowerbed[i]==0:
                # border condition
                if i+1==length:
                    n -= 1
                    i += 1
                # 如果能种则令n减一，然后这个位置就按照遇到1时处理，即跳两格
                elif flowerbed[i+1]==0:
                    n -= 1
                    i += 2
                # 如果index的后一格是1，说明这个位置不能种花且之后两格也不可能种花，直接跳过3格
                else:
                    i += 3
        # 当n减为0时，说明可以种入n朵花，则可以直接退出遍历返回true
        return n==0

# @lc code=end

