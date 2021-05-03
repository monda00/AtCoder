import math

n = int(input())
sqrt_n = int(math.sqrt(n))

ans = list()
for i in range(1, sqrt_n+1):
    if n % i == 0:
        ans.append(i)
        if n/i != i:
            ans.append(n//i)

ans.sort()

for a in ans:
    print(a)
