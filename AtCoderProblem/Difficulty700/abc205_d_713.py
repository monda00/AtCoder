import bisect

n, q = map(int, input().split())
A = list(map(int, input().split()))
K = []
for _ in range(q):
    K.append(int(input()))

A.sort()

C = [A[0]-1]
for i in range(1, len(A)):
    C.append(A[i]-A[i-1]+C[i-1]-1)

for k in K:
    if C[-1] < k:
        print(A[-1]+k-C[-1])
    else:
        ind = bisect.bisect_left(C, k)
        print(A[ind]-1 - (C[ind]-k))
