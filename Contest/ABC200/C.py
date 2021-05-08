import math

n = int(input())
A = list(map(int, input().split()))


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


ans = 0
rem = [0] * 200
for i in range(n):
    rem[A[i] % 200] += 1

for i in range(200):
    if rem[i] > 1:
        ans += combinations_count(rem[i], 2)

print(ans)
