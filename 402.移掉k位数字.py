#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        for n in num:
            while k and numStack and numStack[-1]>n:
                numStack.pop()
                k -= 1
            numStack.append(n)
        
        final = numStack[:-k] if k else numStack

        return ''.join(final).lstrip('0') or '0'

# @lc code=end

