from collections import Counter

n, k = map(int, input().split())
A = list(map(int, input().split()))

C = Counter(A)
C = sorted(C.values())

ans = 0

for i in range(len(C)-k):
    ans += C[i]

print(ans)
