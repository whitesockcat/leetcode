a = [[0, 1, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1]]

class Test():
    def __init__(self):
        self.lst = []

    def dfs(self, a, mark, directions, i, j, n):
        if [i, j] not in self.lst:
            self.lst.append([i, j])
        mark[i][j] = True
        for d in directions:
            r = i + d[0]
            s = j + d[1]
            if 0<=r<n and 0<=s<n and a[r][s]==1 and mark[r][s] ==False:
                if [r,s] not in self.lst:
                    self.lst.append([r,s])
                self.dfs(a, mark, directions, r, s, n)
        return None

    def corr(self, a):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(a)
        mark = [[False]*n for _ in range(n)]
        lsts = []
        for i in range(n):
            for j in range(n):
                if a[i][j] == 1 and mark[i][j] == False:
                    self.lst = []
                    self.dfs(a, mark, directions, i, j, n)
                    lsts.append(self.lst.copy())
        return lsts

solver = Test()
lsts = solver.corr(a)
for i in range(len(lsts)):
    print(lsts[i])