'''
[C - Monsters Battle Royale](https://atcoder.jp/contests/abc118/tasks/abc118_c)
'''

import math

n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n):
    ans = math.gcd(ans, a[i])

print(ans)
