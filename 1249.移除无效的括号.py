#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack0, stack1, o = [], [], ''
        for i, c in enumerate(s):
            if c == '(':
                stack0.append(i)
            elif c == ')':
                if stack0:
                    stack0.pop()
                else:
                    stack1.append(i)
        # 在set里查找很快,比list快10倍
        indexes_to_remove = set(stack0).union(set(stack1))
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                o += c
        return o

# @lc code=end

