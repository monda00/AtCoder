n, m = map(int, input().split())
A = []
B = []
C = []
D = []

for _ in range(m):
    a, b = map(int, input().split())
    A.append(a-1)
    B.append(b-1)

k = int(input())
for _ in range(k):
    c, d = map(int, input().split())
    C.append(c-1)
    D.append(d-1)


pattern = []
for i in range(2**(k)):
    put = [0 for _ in range(k)]
    for j in range(k):
        if i >> j & 1:
            put[j] = 1
    pattern.append(put)


ans = 0
for pat in pattern:
    dish = [0 for _ in range(n)]
    for i, p in enumerate(pat):
        if p == 0:
            dish[C[i]] = 1
        else:
            dish[D[i]] = 1

    tmp = 0
    for i in range(m):
        if dish[A[i]] == 1 and dish[B[i]] == 1:
            tmp += 1
    if ans < tmp:
        ans = tmp

print(ans)
