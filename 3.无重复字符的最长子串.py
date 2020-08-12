#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxlen = 0
        # stack = []
        # back = 0
        # l = 0
        # for ch in s:
        #     if ch not in stack:
        #         l += 1
        #     else:
        #         back = stack.index(ch)
        #         l -= back
        #         stack = stack[back+1:]
        #     stack.append(ch)
        #     maxlen = max(maxlen, l)
        # return maxlen
            
        back, maxlen, c_dict = -1, 0, {}
        for i, ch in enumerate(s):
            if ch in c_dict and c_dict[ch] > back:
                back = c_dict[ch]
                c_dict[ch] = i
            else:
                c_dict[ch] = i
                maxlen = max(maxlen, i-back)
        return maxlen
            
# @lc code=end

