#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack, remain = [], ''
        for ch in S:
            if ch == ')':
                stack.pop()
                if stack:
                    remain += ch
            else:
                stack.append(ch)
                if len(stack)>1:
                    remain += ch
        return remain
# @lc code=end

