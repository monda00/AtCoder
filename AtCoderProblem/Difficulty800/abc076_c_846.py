'''
[C - Dubious Document 2](https://atcoder.jp/contests/abc076/tasks/abc076_c)
'''

s = list(input())
t = list(input())

s_n = len(s)
t_n = len(t)

ans_li = []
for i in range(s_n-t_n, -1, -1):
    for j in range(t_n):
        if s[i+j] != '?' and s[i+j] != t[j]:
            break
        if j == t_n-1:
            tmp = s.copy()
            tmp[i:i+t_n] = t
            ans_li.append(tmp)

ans = []
for a in ans_li:
    for i in range(s_n):
        if a[i] == '?':
            a[i] = 'a'
    ans.append(a)

if len(ans) == 0 or s_n < t_n:
    print('UNRESTORABLE')
else:
    ans.sort()
    print(''.join(ans[0]))
