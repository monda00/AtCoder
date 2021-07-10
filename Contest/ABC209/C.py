n = int(input())
C = list(map(int, input().split()))

C.sort()
ans = 1
for i in range(n):
    if C[i] - i < 0:
        ans = 0
        break
    ans *= (C[i] - i)
    ans %= 10**9+7

print(ans)
