n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    if A[i] <= 10:
        continue
    else:
        ans += (A[i] - 10)

print(ans)
