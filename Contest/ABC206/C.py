import collections

n = int(input())
A = list(map(int, input().split()))

A_c = collections.Counter(A)

ans = 0
for i in range(n):
    ans += i
    A_c[A[i]] -= 1
    ans -= A_c[A[i]]

print(ans)
