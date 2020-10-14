#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        if len(strs) == 0:
            return ans
        for s in zip(*strs):# zip(*) 返回元组
            tmp = set(s)
            if len(tmp) == 1:
                ans += s[0]
            else:
                break
        return ans
# @lc code=end

