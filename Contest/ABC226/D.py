from itertools import combinations
from math import gcd

n = int(input())
X = []
Y = []

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

com = combinations([i for i in range(n)], 2)

s = set()

for c in com:
    x = X[c[0]] - X[c[1]]
    y = Y[c[0]] - Y[c[1]]
    gc = gcd(x, y)
    s.add(str(x//gc)+' '+str(y//gc))
    s.add(str(-1 * x//gc)+' '+str(-1 * y//gc))

ans = len(list(s))
print(ans)
