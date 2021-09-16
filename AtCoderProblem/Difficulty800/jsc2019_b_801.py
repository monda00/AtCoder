n, k = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7

ans = 0

for i in range(n):
    before_min = sum(A[i] > x for x in A[:i])
    after_min = sum(A[i] > x for x in A[i:])

    ans += ((k * (k+1))//2) * after_min
    ans += ((k * (k-1))//2) * before_min

    ans %= mod

print(ans)
