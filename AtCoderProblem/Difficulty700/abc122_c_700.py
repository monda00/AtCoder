'''
[C - GeT AC](https://atcoder.jp/contests/abc122/tasks/abc122_c)
'''

import bisect

n, q = map(int, input().split())
s = list(input())
l = []
r = []
for _ in range(q):
    l_inp, r_inp = map(int, input().split())
    l.append(l_inp-1)
    r.append(r_inp-1)

ac_ind = []
for i in range(n-1):
    if s[i] + s[i+1] == 'AC':
        ac_ind.append(i)

for i in range(q):
    s = bisect.bisect_left(ac_ind, l[i])
    t = bisect.bisect_left(ac_ind, r[i])
    print(t - s)
