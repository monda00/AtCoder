from collections import deque

n = int(input())
A = list(map(int, input().split()))

b = deque()
for i in range(n):
    if i % 2 == 0:
        b.append(A[i])
    else:
        b.appendleft(A[i])

if n % 2 == 1:
    b.reverse()

print(*b)
