#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n=len(dungeon), len(dungeon[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i < m-1 and j < n-1:
                    dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
                elif i == m-1 and j!= n-1:
                    dp[i][j] = max(dp[i][j+1] - dungeon[i][j], 1)
                elif j==n-1 and i !=  m-1:
                    dp[i][j] = max(dp[i+1][j] - dungeon[i][j], 1)
                else:
                    dp[m-1][n-1] = max(1-dungeon[m-1][n-1], 1)
        return dp[0][0]
# @lc code=end

