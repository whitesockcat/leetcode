# 楼梯长n, 一步最大迈m格，每一步和前两步都不同，求走法数量
import numpy as np
n, m = 7, 3
# expected_out = 2

dp = [[[0]*(m+1) for _ in range(m+1)] for _ in range(n+1)]
# dp[1][1][0] = 1
# dp[2][2][0] = 1
# dp[3][3][0] = 1
# dp[3][2][1] = 1
# dp[3][1][2] = 1
# print(dp[1][1][0])
for i in range(1, n+1):
    for j in range(1, i+1):
        if j > m:
            continue
        for k in range(m+1):
            if j == 0:
                continue
            if j == k:
                continue
            if j + k > i:
                continue
            if k == 0 and i == j:
                dp[i][j][k] = 1
            else:
                dp[i][j][k] = sum(dp[i-j][k]) - dp[i-j][k][j]
            # print(i, j, k, dp[i][j][k])
print(np.sum(dp[-1]))
