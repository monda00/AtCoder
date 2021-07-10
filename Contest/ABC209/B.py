n, x = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 1:
        A[i] = A[i] - 1

if x >= sum(A):
    print('Yes')
else:
    print('No')
