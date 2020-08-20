#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += n // 5
            n = n // 5
        return cnt
# @lc code=end

