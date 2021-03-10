'''
[D - Powerful Discount Tickets](https://atcoder.jp/contests/abc141/tasks/abc141_d)
'''

import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

for i in range(m):
    max_a = A[-1]
    A.pop(-1)
    half = max_a//2
    bisect.insort(A, half)

ans = sum(A)

print(ans)
