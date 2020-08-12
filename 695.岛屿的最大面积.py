#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(m, n, i, j, marked, grid, direction):
            marked[i][j] = True
            cnt = 1
            for d in direction:
                r = i + d[0]
                s = j + d[1]
                if 0<=r<m and 0<=s<n and grid[r][s] == 1 and marked[r][s] == False:
                    cnt += dfs(m,n,r,s,marked,grid, direction)
            return cnt

        direction = [(0,-1),(-1,0),(0,1),(1,0)]
        m = len(grid)
        if not m:   return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        maxcnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and marked[i][j] == False:
                    cnt = dfs(m,n,i,j,marked,grid, direction)
                    maxcnt = max(maxcnt, cnt)
        return maxcnt
        
# @lc code=end

