#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack0 = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.stack0 and self.stack0[-1] < x:
            self.stack0.append(self.stack0[-1])
        else:
            self.stack0.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.stack0.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack0[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

