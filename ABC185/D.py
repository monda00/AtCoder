import math

n, m = map(int, input().split())
if m != 0:
    A = list(map(int, input().split()))
    A.sort()
else:
    print(1)
    exit()

diff = list()
if A[0]-1 != 0:
    diff.append(A[0]-1)
for i in range(m-1):
    if A[i+1]-A[i]-1 != 0:
        diff.append(A[i+1]-A[i]-1)

if n-A[-1] != 0:
    diff.append(n-A[-1])

if len(diff) == 0:
    print(0)
    exit()
else:
    min_diff = min(diff)

ans = 0
for i in range(len(diff)):
    ans += math.ceil(diff[i]/min_diff)

print(ans)
