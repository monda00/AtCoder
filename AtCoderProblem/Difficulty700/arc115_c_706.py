'''
[C - ℕ Coloring](https://atcoder.jp/contests/arc115/tasks/arc115_c)
'''

import math

n = int(input())

ans = [1]
max_v = 1
for i in range(2, n+1):
    if 2**max_v == i:
        max_v += 1
        ans.append(max_v)
    else:
        ans.append(max_v)

print(*ans)
