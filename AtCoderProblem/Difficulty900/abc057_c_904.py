'''
[C - Digits in Multiplication](https://atcoder.jp/contests/abc057/tasks/abc057_c)
'''

import math

n = int(input())

sqrt_n = int(math.sqrt(n))
ans = 10**10+1
for i in range(1, sqrt_n+2):
    a = i
    b = n//a

    if a * b == n:
        cur = max(len(str(a)), len(str(b)))
        if ans > cur:
            ans = cur

print(ans)
