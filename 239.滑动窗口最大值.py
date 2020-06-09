#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
# 法一，暴力法，超时
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i: i+k]))
        return res

# 法二，双端队列
# 视频见https://leetcode-cn.com/problems/sliding-window-maximum/solution/shi-pin-jie-xi-shuang-duan-dui-lie-hua-dong-chuang/
import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            # deque[0]对应的下标超过了窗口范围，去掉
            while deque and deque[0] <= i - k: 
                deque.popleft() # outdate indices
            while deque and num > nums[deque[-1]]: 
                deque.pop()
            deque.append(i)
            # deque[0]始终存放该窗口内最大的值对应的下标
            if i >= k - 1:
                res.append(nums[deque[0]])
        return res

# @lc code=end

