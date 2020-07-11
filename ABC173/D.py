import math
n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = A[0] + 2*sum(A[1:math.floor(n/2)]) + (n%2)*A[math.floor(n/2)]
print(ans)
