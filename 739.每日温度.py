#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for idx, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                cur = stack.pop()
                res[cur] = idx - cur
            stack.append(idx)
        return res
        
# @lc code=end

