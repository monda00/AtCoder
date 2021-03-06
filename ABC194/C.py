n = int(input())
A = list(map(int, input().split()))

ans = 0
sum_a = sum(A)
for i in range(n):
    sum_a -= A[i]
    ans += (n-1)*A[i]**2 - 2*A[i]*sum_a

print(ans)
