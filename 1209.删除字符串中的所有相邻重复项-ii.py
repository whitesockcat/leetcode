#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack_c, stack_n = [], []
        # for c in s:
        #     if stack_c and c == stack_c[-1]:
        #         stack_n[-1][1] += 1
        #         if stack_n[-1][1] == k:
        #             start_i, _ = stack_n.pop()
        #             stack_c = stack_c[:start_i]
        #         else:
        #             stack_c.append(c)
        #     else:
        #         stack_n.append([len(stack_c), 1])
        #         stack_c.append(c)
        #     # print(stack_c)
        #     # print(stack_n)
        # return ''.join(stack_c)

        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c*k for c, k in stack)
# @lc code=end

