n, s, d = map(int, input().split())
X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(n):
    if X[i] < s and Y[i] > d:
        print('Yes')
        exit()

print('No')
