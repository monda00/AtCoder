'''
[D - Binomial Coefficients](https://atcoder.jp/contests/abc094/tasks/arc095_b)
'''

import math

n = int(input())
a = list(map(int, input().split()))
a.sort()
a_max = max(a)
a = a[:-1]

d = []
for i in range(n-1):
    d.append(abs(a_max/2 - a[i]))

print(a_max, a[d.index(min(d))])
