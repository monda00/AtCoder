'''
[C - Good Sequence](https://atcoder.jp/contests/abc082/tasks/arc087_a)
'''

import collections

n = int(input())
A = list(map(int, input().split()))
A.sort()
A = collections.Counter(A)

ans = 0
for a_i, a_v in A.items():
    if a_i > a_v:
        ans += a_v
    elif a_i < a_v:
        ans += (a_v - a_i)

print(ans)
