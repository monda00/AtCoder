'''
[A - Biscuits](https://atcoder.jp/contests/agc017/tasks/agc017_a)
'''

import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, p = map(int, input().split())
A = list(map(int, input().split()))

even = len([i for i in range(n) if A[i] % 2 == 0])
odd = len([i for i in range(n) if A[i] % 2 == 1])

ans = 0

for i in range(even+1):
    for j in range(odd//2+1):
        ans += combinations_count(even, i) * combinations_count(odd, j*2)

if p == 1:
    ans = 2**n - ans

print(ans)
