'''
[A - Not coprime](https://atcoder.jp/contests/arc114/tasks/arc114_a)
'''

from math import gcd

n = int(input())
X = list(map(int, input().split()))

factors = [2, 3]
for num in range(2, 50):
    i = 2
    while i <= num:
        if (num % i == 0):
            break
        elif(i == int(num / 2)):
            factors.append(num)
        i += 1

P = 1 << len(factors)

ans = 10**20

for i in range(P):
    y = 1
    flag = True
    for j in range(len(factors)):
        if i & 1 << j:
            y *= factors[j]

    for k in range(n):
        if gcd(X[k], y) == 1:
            flag = False
            break

    if flag and y != 1:
        ans = min(ans, y)

print(ans)
