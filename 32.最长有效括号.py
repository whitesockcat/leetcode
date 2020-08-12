#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack and s[stack[-1]] == '(':    
                    stack.pop()
                    continue
            stack.append(i)
        max_length = 0
        next_index = len(s)
        while stack:
            cur_index = stack.pop()
            cur_length = next_index - cur_index - 1
            max_length = max(max_length, cur_length)
            next_index = cur_index
        max_length = max(max_length, next_index)
        return max_length
# @lc code=end

