#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
# 两个栈，同步更新
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 主栈
        self.stack = []
        # 辅助栈
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 最小栈与主栈同步更新，最小栈每次append当前的最小值
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

