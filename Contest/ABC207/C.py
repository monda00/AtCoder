n = int(input())
T = []
L = []
R = []
for _ in range(n):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.1
    if t == 3:
        l += 0.1
    if t == 4:
        r -= 0.1
        l += 0.1
    T.append(t)
    L.append(l)
    R.append(r)

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if L[i] <= L[j] <= R[i]:
            ans += 1
        elif L[j] <= L[i] <= R[j]:
            ans += 1

print(ans)
