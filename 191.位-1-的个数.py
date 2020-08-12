#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        while n:
            bits += 1
            # n -= n & (~n + 1)
            n &= n-1
        return bits
# @lc code=end

