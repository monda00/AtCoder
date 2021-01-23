n = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(n):
    tmp = A[i]
    for j in range(i, n):
        tmp = min(tmp, A[j])
        ans = max(ans, tmp*(j-i+1))

print(ans)
