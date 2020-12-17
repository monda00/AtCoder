'''
[C - Attention](https://atcoder.jp/contests/arc098/tasks/arc098_a)
'''

import collections

n = int(input())
s = list(input())

s_cnt = collections.Counter(s)
w_sum = s_cnt['W']
e_sum = s_cnt['E']

left_w = 0
left_e = 0
ans = 3*10**5 + 1
for i in range(n):
    if s[i] == 'W':
        tmp = left_w + (e_sum - left_e)
        left_w += 1
    else:
        tmp = left_w + (e_sum - left_e) - 1
        left_e += 1
    if tmp < ans:
        ans = tmp

print(ans)
