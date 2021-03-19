'''
[C - String Invasion](https://atcoder.jp/contests/arc113/tasks/arc113_c)
'''

import collections
from typing import Counter

s = list(input())
n = len(s)

ans = 0
c = collections.Counter()

for i in range(n-1, -1, -1):
    if i+1 < n and s[i] == s[i+1]:
        for k in c.keys():
            if k != s[i]:
                ans += c[k]
        c = Counter()
        c[s[i]] = n - i
    else:
        c[s[i]] += 1

print(ans)
