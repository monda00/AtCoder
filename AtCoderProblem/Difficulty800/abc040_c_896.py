'''
[C - 柱柱柱柱柱](https://atcoder.jp/contests/abc040/tasks/abc040_c)
'''

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n)
for i in range(n):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = dp[i-1]+abs(a[i-1]-a[i])
    elif dp[i-2]+abs(a[i-2]-a[i]) < dp[i-1]+abs(a[i-1]-a[i]):
        dp[i] = dp[i-2]+abs(a[i-2]-a[i])
    else:
        dp[i] = dp[i-1]+abs(a[i-1]-a[i])

ans = dp[n-1]
print(ans)
