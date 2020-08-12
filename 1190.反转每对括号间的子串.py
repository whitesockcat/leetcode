#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack.append(cur)
                cur = ''
            elif c == ')':
                if stack:
                    cur = '{}{}'.format(stack.pop(), cur[::-1])
            else:
                cur += c
        return cur
# @lc code=end

