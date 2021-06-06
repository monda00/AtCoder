n = int(input())
T = list(map(int, input().split()))
tot = sum(T)
dp = [False] * (tot + 1)
dp[0] = True

for t in T:
    for i in range(tot+1)[::-1]:
        if dp[i]:
            dp[i+t] = True

ans = tot

for i in range(tot+1):
    if dp[i]:
        tmp = max(i, tot-i)
        ans = min(ans, tmp)

print(ans)
