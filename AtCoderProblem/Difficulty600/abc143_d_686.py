'''
[D - Triangles](https://atcoder.jp/contests/abc143/tasks/abc143_d)
'''

import bisect

n = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i in range(n):
    for j in range(i+1, n):
        k = bisect.bisect_left(L, L[i]+L[j])
        ans += k - j - 1

print(ans)
