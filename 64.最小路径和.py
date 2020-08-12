#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i == 0 and j!= 0:
                    dp[0][j] = dp[0][j-1] + grid[0][j]
                elif j==0 and i != 0:
                    dp[i][0] = dp[i-1][0] + grid[i][0]
                else:
                    dp[0][0] = grid[0][0]
        return dp[m-1][n-1]
# @lc code=end

