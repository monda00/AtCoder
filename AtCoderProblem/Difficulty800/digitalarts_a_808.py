'''
[A - C-Filter](https://atcoder.jp/contests/digitalarts2012/tasks/digitalarts_1)
'''

import re


S = list(input().split(' '))
n = int(input())
t = []
for _ in range(n):
    t.append(input().replace('*', '.'))

ans = []

for s in S:
    flag = True
    for ng in t:
        pat = re.compile(ng)
        m = re.fullmatch(pat, s)
        if not m is None:
            ans.append('*'*len(s))
            flag = False
            break
    if flag:
        ans.append(s)

print(' '.join(ans))
