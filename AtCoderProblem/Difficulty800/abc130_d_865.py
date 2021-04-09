'''
[D - Enough Array](https://atcoder.jp/contests/abc130/tasks/abc130_d)
'''

import bisect
import itertools

n, k = map(int, input().split())
a = list(map(int, input().split()))
X = [0] + list(itertools.accumulate(a))
ans = 0

for x in X:
    ind = bisect.bisect_left(X, k+x)
    if ind <= n:
        ans += n - ind + 1

print(ans)
