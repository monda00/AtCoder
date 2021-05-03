n, m = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
a = [int(input()) for i in range(m)]
dp = [0 for i in range(n+1)]
dp[0] = 1
for i in range(m):
    dp[a[i]] = -1


for i in range(n):
    if dp[i] != -1:
        if dp[i+1] != -1:
            dp[i+1] += dp[i] % mod

        if i != n-1 and dp[i+2] != -1:
            dp[i+2] += dp[i] % mod

print(dp[-1] % mod)

