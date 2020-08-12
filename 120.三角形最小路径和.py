#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # # O(n2)空间
        # n = len(triangle)
        # dp = [[0] * n for _ in range(n)]
        # for i in range(n-1,-1,-1):
        #     for j in range(i+1):
        #         if i == n-1:
        #             dp[i][j] = triangle[i][j]
        #         else:
        #             dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        # return dp[0][0]

        # # O(2n)空间
        # n = len(triangle)
        # dp = [[0]*n for _ in range(2)]
        # if n == 1:
        #     return triangle[0][0]
        # for i in range(n-1,-1,-1):
        #     if i == n-1:
        #         dp[1] = triangle[i]
        #     else:
        #         for j in range(i+1):
        #             if i == n-1:
        #                 dp[1][j] = triangle[i][j]
        #             else:
        #                 dp[0][j] = min(dp[1][j], dp[1][j+1]) + triangle[i][j]
        #         dp[1] = dp[0]
        # return dp[0][0]

        # O(n)空间
        n = len(triangle)
        dp = [0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1):
                if i == n-1:
                    dp[j] = triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
# @lc code=end

