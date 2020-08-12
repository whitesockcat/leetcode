#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # # dp
        # if n < 3:
        #     return n
        # dp = {}
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # # dp less place
        # p,q,r = 0,0,1
        # for _ in range(n):
        #     p = q
        #     q = r
        #     r = p + q
        # return r

        # # 斐波那契数列的公式
        import math
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(fibn/sqrt5)

# @lc code=end

