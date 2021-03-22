'''
[C - 友達の友達](https://atcoder.jp/contests/abc016/tasks/abc016_3)
'''

n, m = map(int, input().split())
A = []
B = []
for _ in range(m):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

f = [[] for _ in range(n)]

for i in range(m):
    f[A[i]].append(B[i])
    f[B[i]].append(A[i])

ff_l = []
for i in range(len(f)):
    s = set()
    for ff in f[i]:
        for j in f[ff]:
            if j != i:
                s.add(j)
    ff_l.append(s)

for i in range(m):
    if B[i] in ff_l[A[i]]:
        ff_l[A[i]].discard(B[i])
    if A[i] in ff_l[B[i]]:
        ff_l[B[i]].discard(A[i])

for i in range(n):
    print(len(ff_l[i]))
