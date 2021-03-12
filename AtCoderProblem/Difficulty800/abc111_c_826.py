'''
[C - /\/\/\/](https://atcoder.jp/contests/abc111/tasks/arc103_a)
'''

import collections

n = int(input())
v = list(map(int, input().split()))

odd = []
even = []

for i in range(n):
    if i % 2 == 0:
        even.append(v[i])
    else:
        odd.append(v[i])

even_c = collections.Counter(even).most_common()
odd_c = collections.Counter(odd).most_common()

if even_c[0] != odd_c[0]:
    ans = n - (even_c[0][1] + odd_c[0][1])
elif len(even_c) == 1 and len(odd_c) == 1:
    ans = n//2
else:
    change_e = n - (even_c[1][1] + odd_c[0][1])
    change_o = n - (even_c[0][1] + odd_c[1][1])
    ans = min(change_e, change_o)

print(ans)
