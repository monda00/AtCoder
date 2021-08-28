'''
https://atcoder.jp/contests/arc116
'''

n = int(input())
A = list(map(int, input().split()))
A.sort()
mod = 998244353

ans = 0
tot = 0
pre = 0
for i in range(n):
    tot += A[i]
    ans += tot*A[i]
    ans %= mod
    tot += pre
    tot %= mod
    pre = tot

print(ans)
