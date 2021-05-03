n = int(input())
X = []

for _ in range(n):
    a, p, x = map(int, input().split())
    X.append([a, p, x])

X.sort(key=lambda x: (x[0], x[2], x[1]))

dis = 0
ans = 10**10 + 1
for i in range(n):
    dis = X[i][0]
    if X[i][2]-dis > 0:
        if ans > X[i][1]:
            ans = X[i][1]


if ans == 10**10+1:
    ans = -1

print(ans)
