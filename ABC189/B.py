n, x = map(int, input().split())
x = x * 100
V = []
P = []
for _ in range(n):
    v, p = map(int, input().split())
    V.append(v)
    P.append(p)

sum_al = 0
for i in range(n):
    al = V[i] * P[i]
    sum_al += al
    if sum_al > x:
        print(i+1)
        exit()

print(-1)
