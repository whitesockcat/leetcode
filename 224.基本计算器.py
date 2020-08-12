#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        # total = 0
        # i, signs = 0, [1, 1]
        # while i < len(s):
        #     c = s[i]
        #     if c.isdigit():
        #         start = i
        #         while i < len(s) and s[i].isdigit():
        #             i += 1
        #         total += signs.pop() * int(s[start:i])
        #         continue
        #     if c in '+-(':
        #         signs += signs[-1] * (1, -1)[c == '-'],
        #     elif c == ')':
        #         signs.pop()
        #     i += 1
        # return total
        total = 0
        i, flag, sign = 0, [], 1
        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                if not flag:
                    total += sign * int(s[start:i])
                else:
                    total += flag[-1] * sign * int(s[start:i])
                continue
            elif c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                if flag:
                    flag.append(flag[-1]*sign)
                else:
                    flag.append(sign)
                sign = 1
            elif c == ')':
                flag.pop()
            i += 1
        return total
# @lc code=end

