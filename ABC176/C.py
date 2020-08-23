N = int(input())
A = list(map(int, input().split()))

step = 0

for i in range(1, N):
    if A[i-1] > A[i]:
        step += A[i-1] - A[i]
        A[i] += A[i-1] - A[i]

print(step)
