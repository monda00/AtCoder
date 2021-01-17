'''
[C - いっしょ](https://atcoder.jp/contests/arc059/tasks/arc059_a)
'''

import math
import numpy as np

n = int(input())
A = list(map(int, input().split()))

a_mf = math.floor(np.mean(A))
a_mc = math.ceil(np.mean(A))

ans_f = 0
ans_c = 0
for a in A:
    ans_f += (a - a_mf)**2
    ans_c += (a - a_mc)**2

if ans_f < ans_c:
    print(ans_f)
else:
    print(ans_c)
