'''
[C - Reconciled?](https://atcoder.jp/contests/abc065/tasks/arc076_a)
'''

import math

n, m = map(int, input().split())

if n == m:
    n_f = math.factorial(n) % (10**9 + 7)
    m_f = math.factorial(m) % (10**9 + 7)
    ans = (n_f * m_f * 2) % (10**9 + 7)
elif abs(n - m) == 1:
    n_f = math.factorial(n) % (10**9 + 7)
    m_f = math.factorial(m) % (10**9 + 7)
    ans = (n_f * m_f) % (10**9 + 7)
else:
    ans = 0

print(ans)
