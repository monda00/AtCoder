import bisect

n, q = map(int, input().split())
A = list(map(int, input().split()))
K = []
for _ in range(q):
    K.append(int(input()))

A.sort()

B = [A[0]-1]
for i in range(1, len(A)):
    B.append(A[i]-A[i-1]+B[i-1]-1)

for k in K:
    if B[-1] < k:
        print(A[-1] + k - B[-1])
    else:
        ind = bisect.bisect_left(B, k)
        print(A[ind] - 1 - (B[ind] - k))
