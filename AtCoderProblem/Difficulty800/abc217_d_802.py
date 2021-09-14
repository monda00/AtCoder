'''
[D - Cutting Woods](https://atcoder.jp/contests/abc217/tasks/abc217_d)
'''

import array
import bisect

l, q = map(int, input().split())
C = []
X = []

for _ in range(q):
    c, x = map(int, input().split())
    C.append(c)
    X.append(x)

a = array.array('i', [0, l])

for i in range(q):
    y = bisect.bisect(a, X[i])
    if C[i] == 1:
        a.insert(y, X[i])
    else:
        print(a[y]-a[y-1])
