n = int(input())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10**6
for i in range(n):
    for j in range(n):
        if i == j:
            tmp = A[i] + B[j]
        else:
            tmp = max(A[i], B[j])
        if ans > tmp:
            ans = tmp

print(ans)
