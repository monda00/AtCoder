'''
[A - 掲示板](https://atcoder.jp/contests/arc042/tasks/arc042_a)
'''

n, m = map(int, input().split())
A = []
for _ in range(m):
    A.append(int(input()))

A = A[::-1]
set_a = set()
ans = []

for a in A:
    if not a in set_a:
        set_a.add(a)
        ans.append(a)

for i in range(1, n+1):
    if not i in set_a:
        ans.append(i)

for a in ans:
    print(a)
