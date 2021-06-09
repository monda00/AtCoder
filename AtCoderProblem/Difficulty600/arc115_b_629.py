'''
[B - Plus Matrix](https://atcoder.jp/contests/arc115/tasks/arc115_b)
'''

import numpy as np
from numpy.ma.core import where

n = int(input())
C = []
for _ in range(n):
    c = list(map(int, input().split()))
    C.append(c)

B = np.min(C, axis=0)
A = []

for i in range(n):
    diff = C[i] - B
    if len(set(diff)) != 1:
        print('No')
        exit()
    else:
        A.append(diff[0])

print('Yes')
print(*A)
print(*B)
