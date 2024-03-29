'''
[C - Special Trains](https://atcoder.jp/contests/abc084/tasks/abc084_c)
'''

n = int(input())

C = []
S = []
F = []
for _ in range(n-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(n):
    t = 0
    for j in range(i, n-1):
        if t < S[j]:
            t = S[j]
        elif t % F[j] == 0:
            t = t
        else:
            t = t + F[j] - t % F[j]
        t += C[j]
    print(t)
