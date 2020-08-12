#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

# @lc code=end

