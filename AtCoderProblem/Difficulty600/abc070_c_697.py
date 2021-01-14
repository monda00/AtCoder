'''
[C - Multiple Clocks](https://atcoder.jp/contests/abc070/tasks/abc070_c)
'''

import math


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


n = int(input())
T = list()
for _ in range(n):
    T.append(int(input()))

ans = 1
for t in T:
    ans = lcm(t, ans)

print(ans)
