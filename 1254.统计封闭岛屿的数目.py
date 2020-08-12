#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#

# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # self.direction = [(0,-1),(-1,0),(0,1),(1,0)]
        # self.m = len(grid)
        # if not self.m:   return 0
        # self.n = len(grid[0])
        # self.marked = [[False for _ in range(self.n)] for _ in range(self.m)]
        # def dfs(i,j,grid):
        #     self.marked[i][j] = True
        #     for d in self.direction:
        #         r = i+d[0]
        #         s = j+d[1]
        #         if 0<=r<self.m and 0<=s<self.n and grid[r][s] == 0 and self.marked[r][s] == False:
        #             if r == 0 or s == 0 or r == self.m-1 or s == self.n-1:
        #                 self.flag = 0
        #             dfs(r,s,grid)
        # cnt = 0
        # for i in range(1,self.m-1):
        #     for j in range(1,self.n-1):
        #         if grid[i][j] == 0 and self.marked[i][j] == False:
        #             self.flag = 1
        #             dfs(i,j,grid)
        #             cnt += self.flag
        # return cnt
        
        # # BFS
        # result = 0
        # directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        # height, width = len(grid), len(grid[0])
        # for i in range(height):
        #     for j in range(width):
        #         if grid[i][j] == 0:
        #             grid[i][j] = 1
        #             # 队列
        #             queue = collections.deque()
        #             queue.append((i, j))
        #             flag = False
        #             while queue:
        #                 x, y = queue.popleft()
        #                 if x == 0 or x == height - 1 or y == 0 or y == width - 1:
        #                     flag = True
        #                 for a, b in directions:
        #                     m, n = x + a, y + b
        #                     if 0 <= m < height and 0 <=n < width and grid[m][n] == 0:
        #                         grid[m][n] = 1
        #                         queue.append((m, n))
        #             if not flag:
        #                 result += 1
        # return result

        # DFS
        result = 0
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        height, width = len(grid), len(grid[0])
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    stack = []
                    stack.append((i, j))
                    flag = False
                    while stack:
                        x, y = stack.pop()
                        if x == 0 or x == height - 1 or y == 0 or y == width - 1:
                            flag = True
                        for a, b in directions:
                            m, n = x + a, y + b
                            if 0 <= m < height and 0 <=n < width and grid[m][n] == 0:
                                grid[m][n] = 1
                                stack.append((m, n))
                    if not flag:
                        result += 1
        return result

# @lc code=end

