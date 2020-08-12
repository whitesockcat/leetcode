#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        j = 0
        cnt = 0
        # for i in range(len(g)):
        #     while j < len(s) and g[i] > s[j]:
        #         j += 1
        #     if j == len(s):
        #         return cnt
        #     else:
        #         cnt += 1
        #         j += 1
        # return cnt
        i = 0
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
            j += 1
        return cnt
# @lc code=end

