#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(m, n, i, j, marked, grid, direction):
            marked[i][j] = True
            for d in direction:
                r = i + d[0]
                s = j + d[1]
                if 0<=r<m and 0<=s<n and grid[r][s] == '1' and marked[r][s] == False:
                    dfs(m,n,r,s,marked,grid, direction)

        direction = [(0,-1),(-1,0),(0,1),(1,0)]
        m = len(grid)
        if not m:   return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and marked[i][j] == False:
                    dfs(m,n,i,j,marked,grid, direction)
                    cnt += 1
        return cnt
# @lc code=end

