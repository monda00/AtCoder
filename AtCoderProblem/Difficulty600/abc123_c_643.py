'''
[C - Five Transportations](https://atcoder.jp/contests/abc123/tasks/abc123_c)
'''

import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

min_n = min([a, b, c, d, e])
ans = math.ceil(n/min_n) + 5 - 1

print(ans)
