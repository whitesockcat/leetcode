

def ZeroOnePack(dp, c, V, v):
    for i in range(V, c-1, -1):
        dp[i] = max(dp[i], dp[i-c] + v)

def CompletePack(dp, c, V, v):
    for i in range(c, V+1):
        dp[i] = max(dp[i], dp[i-c] + v)


costs = [2,2,1,2]
values = [4,35,43,10]
n = 4
V = 6
dp = [0] * (V+1)
for i in range(n):
    CompletePack(dp, costs[i], V, values[i])

print(dp)